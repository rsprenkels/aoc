# solution to https://adventofcode.com/2022/day/23
import copy
from collections import defaultdict, namedtuple
from typing import List
import re
from dataclasses import dataclass

aoc_day_number = '23'

@dataclass(frozen=True)
class P:
    x: int
    y: int

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)


def get_tiles_at(target_time, tiles_in_time):
    def get_next(t):
        return t

    if target_time not in tiles_in_time:
        tiles_in_time[target_time] = get_next(tiles_in_time[target_time - 1])
    return tiles_in_time[target_time]


def solution(lines: List[str], part=1):
    tiles_in_time = {}
    t0 = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            t0[P(x, y)] = c
    start = list(t for t in t0 if t.y == 0 and t0[t] == '.')[0]
    finish = list(t for t in t0 if t.y == len(lines)-1 and t0[t] == '.')[0]
    tiles_in_time[0] = t0
    queue = [(0, start)]
    while queue:
        minute, location = queue.pop(0)
        tx = get_tiles_at(minute + 1, tiles_in_time)

demo_input = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".split('\n')


def test_demo_input_part1():
    print()
    round_number, area = solution([l for l in demo_input])
    assert area == 110

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

# def test_demo_input_part2():
#     print()
#     assert solution([l for l in demo_input], part=2) == 5031

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')


