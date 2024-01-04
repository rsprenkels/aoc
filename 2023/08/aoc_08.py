import collections
import itertools
import locale
import math
from collections import defaultdict
from functools import cache, cmp_to_key
from typing import List
import re

day_number = '08'


def sol_part1(lines: List[str], part = 1) -> int:
    directions = itertools.cycle(enumerate(list(lines[0])))
    T = dict()
    for line in lines[2:]:
        T[line[0:3]] = tuple(line[7:15].split(', '))
    if part == 1:
        step_count = 0
        cur_node = 'AAA'
        while cur_node != 'ZZZ':
            step_count += 1
            if next(directions)[1] == 'L':
                cur_node = T[cur_node][0]
            else:
                cur_node = T[cur_node][1]
        return step_count
    else:
        nodes = [n for n in T.keys() if n[2] == 'A']
        periods = []
        for node in nodes:
            directions = itertools.cycle(enumerate(list(lines[0])))
            step_count = 0
            cur_node = node
            z_nodes_found = []
            seen = []
            cycle_detected = False
            while not cycle_detected:
                step_count += 1
                next_dir = next(directions)
                if (cur_node, next_dir) in seen:
                    cycle_detected = True
                seen.append((cur_node, next_dir))
                if next_dir[1] == 'L':
                    cur_node = T[cur_node][0]
                else:
                    cur_node = T[cur_node][1]
                if cur_node[2] == 'Z':
                    z_nodes_found.append(step_count)
            periods.append(int(z_nodes_found[0]))
        return math.lcm(*periods)
        # 60177485833 is too low. one more: also.
        # 60177485837
        # 16187743689077


def sol_part2(lines):
    return sol_part1(lines, part=2)

lines_1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""[1:-1].split('\n')

def test_01():
    assert sol_part1(lines_1) == 2

def test_02():
    lines = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""[1:-1].split('\n')
    assert sol_part2(lines) == 6

if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day {day_number} part 1:{sol_part1(lines)}')
    print(f'day {day_number} part 2:{sol_part2(lines)}')


