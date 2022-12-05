# solution to https://adventofcode.com/2022/day/4
import logging
from typing import Tuple

aoc_day_number = '04'
logging.basicConfig(level=logging.DEBUG)

def fully_contains(a : Tuple[int, int], b: Tuple[int, int]) -> bool:
    return a[0] >= b[0] and a[1] <= b[1]

def partly_overlaps(a : Tuple[int, int], b: Tuple[int, int]) -> bool:
    # return a[1] <= b[0] or b[1] >= a[0]
    return (a[0] <= b[0] and a[1] >= b[0]) or a[0] <= b[1] and a[1] >= b[1]

def solution(lines, count_function=fully_contains):
    count = 0
    for elv_pair in lines:
        logging.debug(f'testing {elv_pair}')
        elve_item_tupels = [tuple(map(int, elv.split('-'))) for elv in elv_pair.split(',')]
        if count_function(*elve_item_tupels) or count_function(*reversed(elve_item_tupels)):
            logging.debug(f'result for {elve_item_tupels} is True')
            count += 1
    return count

def test_demo_input():
    lines = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split('\n')
    assert solution(lines) == 2
    assert solution(lines, count_function=partly_overlaps) == 4

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, count_function=partly_overlaps)}', end='')
