# solution to https://adventofcode.com/2022/day/16
import functools
import itertools
from collections import defaultdict
from functools import cmp_to_key
from itertools import permutations
from math import sqrt, ceil
import logging as log
from typing import List, Tuple, Dict
from bitarray import bitarray
from collections import namedtuple

aoc_day_number = '16'


def calc_flowrate(topo, path_through_topo) -> int:
    total_flow = 0
    for t, a, v in path_through_topo:
        if a == 'open':
            total_flow += (30 - t) * topo[v][0]
    return  total_flow

def shortest_path(topo, v_from, v_to):
    prev_results = dict()
    key = tuple(sorted((v_from, v_to)))
    if key in prev_results:
        return prev_results[key]
    else:
        seen = {}
        to_visit = [(0, v_from)]
        while to_visit:
            cost, valve = to_visit.pop(0)
            if valve not in seen or seen[valve] > cost:
                seen[valve] = cost
                for reachable_valve in topo[valve][1]:
                    to_visit.append((cost + 1, reachable_valve))
        prev_results[key] = seen[v_to]
        return seen[v_to]


def flowrate(topo, opened_valves: Dict[str, int], duration: int) -> int:
    '''
    :param topo: per valve (the key) its flowrate and a list of directly reachable valves
    :param opened_valves: dict containing per valve(the key) the time of opening it (the value)
    :param duration: total flowrate is calculated for this point in time
    :return: flowrate at t=duration
    '''
    return sum((duration - open_time) * topo[valve][0] for valve, open_time in opened_valves.items())


def open_valves(topo: Dict[str, Tuple[int, List[str]]], relevant_valves: List[str], duration: int=30):
    '''

    :param topo: per valve the flowrate, and the list of direct tunnels to other valves
    :param relevant_valves: List[valve]
    :param duration: the max available time for finding a path

    :return: List[Tuple[str, int]]  a list of when each valve was opened

    '''
    # print(f'relevant valves:{relevant_valves}')
    queue = []
    seen = {}
    Item = namedtuple("Item", "cur_time cur_valve dest_valve opened_valves")
    for valve in relevant_valves:
        queue.append(Item(cur_time=0, cur_valve='AA', dest_valve=valve, opened_valves={}))
    while queue:
        item = queue.pop(0)
        time_leaving_dest_valve = 1 + item.cur_time + shortest_path(topo, v_from=item.cur_valve, v_to=item.dest_valve)
        if time_leaving_dest_valve > duration:
            continue
        (new_opened_valves := {k:v for k,v in item.opened_valves.items()})[item.dest_valve] = time_leaving_dest_valve
        if (k := tuple(sorted(new_opened_valves))) not in seen or seen[k] < flowrate(topo, new_opened_valves, duration):
            seen[k] = flowrate(topo, new_opened_valves, duration)
            for valve in set(relevant_valves) - set(new_opened_valves):
                queue.append(Item(cur_time=time_leaving_dest_valve, cur_valve=item.dest_valve, dest_valve=valve, opened_valves=new_opened_valves))
    return max(seen.values())


def solution(scan_lines: List[str], part=1):
    topo = {}
    non_zero_valves = 0
    for line in scan_lines:
        p = line.split(' ')
        valve_label = p[1]
        rate = int(p[4][5:-1])
        reachable = line[line.find('valve'):].replace('valve', '').replace('s', '')[1:].split(', ')
        # print(f'valve_label:{valve_label} rate:{rate} reachable:{reachable}')
        topo[valve_label] = (rate, reachable)
        if rate > 0:
            non_zero_valves += 1
    relevant_valves = [valve for valve, (rate, reachable) in topo.items() if rate > 0]
    if part == 1:
        max_rate = open_valves(topo, relevant_valves, duration=30)
        return max_rate
    else:
        best_total = 0
        for elephant_does_thismany in range(1, len(relevant_valves)):
            for p in itertools.combinations(relevant_valves, elephant_does_thismany):
                elephant_rate = open_valves(topo, list(p), duration=26)
                my_rate = open_valves(topo, list(set(relevant_valves) - set(p)), duration=26)
                best_total = max(best_total, elephant_rate + my_rate)
        return best_total


demo_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split('\n')

# def test_shortest_path(scan_lines = demo_input):
#     topo = {}
#     non_zero_valves = 0
#     for line in scan_lines:
#         p = line.split(' ')
#         valve_label = p[1]
#         rate = int(p[4][5:-1])
#         reachable = line[line.find('valve'):].replace('valve', '').replace('s', '')[1:].split(', ')
#         # print(f'valve_label:{valve_label} rate:{rate} reachable:{reachable}')
#         topo[valve_label] = (rate, reachable)
#         if rate > 0:
#             non_zero_valves += 1
#     for valve in topo:
#         print(f'from AA to {valve} is {shortest_path(topo, v_from="AA", v_to=valve)}')


def test_demo_input_part1():
    assert solution([l for l in demo_input]) == 1651

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

# def test_demo_input_part2():
#     assert solution([l for l in demo_input], part=2) == 1707
#
# def test_part_2():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')


