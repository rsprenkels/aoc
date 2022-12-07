# solution to https://adventofcode.com/2022/day/7
import logging
from collections import defaultdict
from typing import Tuple

aoc_day_number = '07'

class Node():
    def __int__(self, rel_path:str):
        self.rel_path = rel_path
        self.children = []

def solution(lines):
    for ndx, line in enumerate(lines):
        if line.startswith('$ cd '):
            cur_dir = Node(line[5:])
        elif line == '$ ls':
            while lines[ndx+1]




def test_demo_input():
    lines = list(open(f'{aoc_day_number}_demo.txt').read().splitlines())
    assert solution([l for l in lines]) == 'CMZ'

#
# def test_part_1():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')
#
#
# def test_part_2():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 2: {solution(lines, execute_transfer=whole_stack)}', end='')
#
