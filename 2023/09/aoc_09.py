import collections
import itertools
import locale
import math
from collections import defaultdict
from functools import cache, cmp_to_key
from typing import List
import re

day_number = '09'

def sol_part1(lines: List[str], part = 1) -> int:
    sum_added_numbers = 0
    for line in lines:
        nl = [list(map(int, line.split()))]
        all_deltas_zero = False
        while not all_deltas_zero:
            nl.append([n2 - n1 for n1, n2 in zip(nl[-1], nl[-1][1:])])
            all_deltas_zero = all(n == 0 for n in nl[-1])
        if part == 1:
            sum_added_numbers += sum(row[-1] for row in nl)
        else:
            result = 0
            for r_index in range (len(nl)-2, -1, -1):
                result = nl[r_index][0] - result
            sum_added_numbers += result
    return sum_added_numbers

def sol_part2(lines):
    return sol_part1(lines, part=2)

lines = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""[1:-1].split('\n')

def test_01():
    assert sol_part1(lines) == 114

def test_02():
    assert sol_part2(lines) == 2

if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day {day_number} part 1:{sol_part1(lines)}')
    print(f'day {day_number} part 2:{sol_part2(lines)}')


