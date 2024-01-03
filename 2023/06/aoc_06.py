import collections
import math
from collections import defaultdict
from functools import cache
from typing import List
import re

day_number = '05'

def sol_part1(lines: List[str], part = 1) -> int:
    times = list(map(int, lines[0][9:].split()))
    distances = list(map(int, lines[1][9:].split()))
    win_combinations = 1
    for time, distance in zip(times, distances):
        wins = len(list((speed * (time - speed) for speed in range(1, time) if speed * (time - speed) > distance)))
        print(f'time:{time}  distance:{distance}  wins:{wins}')
        win_combinations *= wins
    return win_combinations

def sol_part2(lines):
    p2_lines = [line[:9] + ''.join(line[9:].split()) for line in lines]
    return sol_part1(p2_lines, part=2)

lines = """
Time:      7  15   30
Distance:  9  40  200
"""[1:-1].split('\n')

def test_01():
    assert sol_part1(lines) == 288

def test_02():
    assert sol_part2(p2_lines) == 71503

if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day {day_number} part 1:{sol_part1(lines)}')
    print(f'day {day_number} part 2:{sol_part2(lines)}')


