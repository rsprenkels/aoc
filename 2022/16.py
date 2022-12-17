# solution to https://adventofcode.com/2022/day/16
from collections import defaultdict
from functools import cmp_to_key
from math import sqrt, ceil
import logging as log
from typing import List, Tuple
from bitarray import bitarray

aoc_day_number = '16'


def calc_flowrate(topo, path_through_topo) -> int:
    total_flow = 0
    for t, a, v in path_through_topo:
        if a == 'open':
            total_flow += (30 - t) * topo[v][0]
    return  total_flow


def solution(scan_lines: List[str], part=1):
    topo = {}
    for line in scan_lines:
        p = line.split(' ')
        valve_label = p[1]
        rate = int(p[4][5:-1])
        reachable = line[line.find('valve'):].replace('valve', '').replace('s', '')[1:].split(', ')
        print(f'valve_label:{valve_label} rate:{rate} reachable:{reachable}')
        topo[valve_label] = (rate, reachable)
    action_queue = [(0, ('open', 'AA'), [])] + [(0, ('goto', node), []) for node in topo['AA'][1]]
    max_flowrate = 0
    loop_count = 0
    while action_queue:
        loop_count += 1
        time_passed, (action, valve), path_so_far = action_queue.pop()
        if time_passed == 30:
            max_flowrate = max(max_flowrate, calc_flowrate(topo, path_so_far))
        else:
            if action == 'open':
                (new_path := [a for a in path_so_far]).append((time_passed + 1, 'open', valve))
                action_queue += [(time_passed + 1, ('goto', node), new_path) for node in topo[valve][1]]
            else:  # did a goto(valve)
                useless_cycle = False
                for ndx, (t, a, v) in enumerate(list(reversed(path_so_far))):
                    if a == 'goto' and v == valve:  # beem here before
                        useless_cycle = len(list(1 for t, a, v in list(reversed(path_so_far))[:ndx] if a == 'open')) == 0
                        break
                if not useless_cycle:
                    (new_path := [a for a in path_so_far]).append((time_passed + 1, 'goto', valve))
                    if valve not in [v for t, a, v in path_so_far if a == 'open'] and topo[valve][0] > 0:
                        action_queue += [(time_passed + 1, ('open', valve), new_path)]
                    action_queue += [(time_passed + 1, ('goto', next_node), new_path) for next_node in topo[valve][1]]
    return max_flowrate

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

# def test_demo_input_part1():
#     assert solution([l for l in demo_input]) == 1651


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')


# def test_part_2():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')
#
#
