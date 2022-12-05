# solution to https://adventofcode.com/2022/day/5
import logging
from collections import defaultdict
from typing import Tuple

aoc_day_number = '05'

def one_by_one(num_items, stack_from, stack_to, stacks):
    for x in range(num_items):
        stacks[stack_to - 1].insert(0, stacks[stack_from - 1].pop(0))


def whole_stack(num_items, stack_from, stack_to, stacks):
    for x in range(num_items):
        stacks[stack_to - 1].insert(0, stacks[stack_from - 1].pop(num_items - x - 1))


def solution(lines, execute_transfer=one_by_one):
    stacks = defaultdict(list)
    while lines[0] != '':
        stack_row = lines.pop(0)
        for item_ndx in range ((len(stack_row) // 4) + 1):
            item = stack_row[item_ndx*4+1]
            if item != ' ':
                stacks[item_ndx].append(item)
    for key in sorted(stacks):
        stacks[key].pop()
    lines.pop(0)
    for instruction in lines:
        parts = instruction.split(' ')
        num_items, stack_from, stack_to = (int(parts[1]), int(parts[3]), int(parts[5]))
        execute_transfer(num_items, stack_from, stack_to, stacks)
    return ''.join(stacks[key][0] for key in sorted(stacks))


def test_demo_input():
    lines = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split('\n')
    assert solution([l for l in lines]) == 'CMZ'
    assert solution(lines, execute_transfer=whole_stack) == 'MCD'


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')


def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, execute_transfer=whole_stack)}', end='')

