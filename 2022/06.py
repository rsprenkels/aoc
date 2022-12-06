# solution to https://adventofcode.com/2022/day/6
import logging
from collections import defaultdict
from typing import Tuple

aoc_day_number = '06'

def solution(line, mark_size=4):
    line = line.rstrip('\n')
    for p in range(len(line) - mark_size):
        if len(set(line[p:p + mark_size])) == mark_size:
            return p + mark_size

def test_demo_input_a():
    assert solution('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10


def test_demo_input_b():
    assert solution('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', mark_size=14) == 29


def test_part_1():
    line = open(f'{aoc_day_number}.txt').readline()
    print(f'\nday {aoc_day_number} part 1: {solution(line)}')
    print(f'day {aoc_day_number} part 2: {solution(line, mark_size=14)}', end='')
