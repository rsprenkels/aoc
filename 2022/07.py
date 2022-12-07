# solution to https://adventofcode.com/2022/day/7
import logging
from collections import defaultdict
from typing import Tuple

aoc_day_number = '07'


class Directory:
    def __init__(self, rel_path: str, parent: str = None):
        self.rel_path = rel_path
        self.children = []
        self.parent = parent


    def __repr__(self):
        return f'Directory({self.rel_path}, p={self.parent}, {self.children})'


def solution(lines):
    cur_dir = None
    dir_stack = []
    file_system = defaultdict(list)
    for ndx, line in enumerate(lines):
        if line.startswith('$ cd '):
            new_dir = line[5:]
            if new_dir == '..':
                cur_dir = dir_stack.pop()
            else:
                dir_stack.append(new_dir)
                cur_dir = Directory(new_dir, cur_dir.)
                file_system[cur_dir.rel_path] = cur_dir
            print(f'dir_stack={dir_stack}')
        elif line == '$ ls':
            ndx += 1
            while ndx < len(lines) and lines[ndx][0] != '$':
                if lines[ndx].startswith('dir '):
                    print(f'I see dir {lines[ndx][4:]}')
                    cur_dir.children.append(lines[ndx][4:])
                else:
                    print(f'I see file {lines[ndx]}')
                    size, filename = lines[ndx].split(' ')
                    cur_dir.children.append((size, filename))
                ndx += 1
    for dir in file_system:
        print(file_system[dir])
    return file_system


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

