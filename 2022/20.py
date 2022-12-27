# solution to https://adventofcode.com/2022/day/20
import copy
from collections import defaultdict, namedtuple
from typing import List
import re

aoc_day_number = '20'

P = namedtuple("P", "ndx, n")


def mix(circle):
    for p in range(len(circle)):
        for c in range(len(circle)):
            if circle[c].ndx == p:
                cur_loc = c
                break
        val = circle.pop(cur_loc)
        new_loc = (cur_loc + val.n) % len(circle)
        if new_loc < cur_loc:
            new_loc = ((new_loc - 1) % len(circle)) + 1
            circle.insert(new_loc, val)
        else:
            circle.insert(new_loc, val)
        # print(f'{val} {cur_loc} {p} rounds: {list(p.n for p in circle)}')

def solution(lines: List[str], part=1):
    circle = []
    for ndx, line in enumerate(lines):
        n = int(line)
        if part == 2:
            n *= 811589153
        circle.append(P(ndx, n))
    mix_this_many_times = 1 if part == 1 else 10
    for _ in range(mix_this_many_times):
        mix(circle)
    for c in range(len(circle)):
        if circle[c].n == 0:
            zero_ndx = c
            break
    total = 0
    for c in range(1000, 4000, 1000):
        total += circle[(zero_ndx + c) % len(circle)].n
    return total


demo_input = """1
2
-3
3
-2
0
4""".split('\n')


def test_demo_input_part1():
    print()
    assert solution([l for l in demo_input]) == 3

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

def test_demo_input_part2():
    print()
    assert solution([l for l in demo_input], part=2) == 1623178306

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')


