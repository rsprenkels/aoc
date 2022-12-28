# solution to https://adventofcode.com/2022/day/22
import copy
from collections import defaultdict, namedtuple
from typing import List
import re

aoc_day_number = '22'

P = namedtuple("P", "ndx, n")


def rotate(cur_direction, direction):
    x, y = cur_direction
    if direction == 'R':
        return -y, x
    else:
        return y, -x


def get_next_loc(cur_loc, cur_direction, map):
    cur_x, cur_y = cur_loc
    next_loc = tuple(a + b for a, b in zip(cur_loc, cur_direction))
    if next_loc in map:
        return next_loc
    else:
        if cur_direction == (1, 0):
            return min(x for x,y in map if y == cur_y), cur_y
        elif cur_direction == (-1, 0):
            return max(x for x,y in map if y == cur_y), cur_y
        elif cur_direction == (0, 1):
            return cur_x, min(y for x,y in map if x == cur_x)
        elif cur_direction == (0, -1):
            return cur_x, max(y for x,y in map if x == cur_x)
        else:
            raise Exception('this should never happen')

def solution(lines: List[str], part=1):
    map = {}
    for y, line in enumerate(lines[:-2]):
        for x, c in enumerate(line):
            if c != ' ':
                map[(x, y)] = c
    cur_loc = (min(x for x, y in map if y == 0), 0)
    cur_direction = (1, 0)
    instructions = lines[-1]
    while instructions:
        if instructions[0].isdigit():
            dist = int((match := re.search(r'^\d+', instructions)).group())
            instructions = instructions[match.end():]
            # print(f'dist:{dist}', end=' ')
            for step in range(dist):
                next_loc = get_next_loc(cur_loc, cur_direction, map)
                if map[next_loc] == '#':
                    break
                else:
                    cur_loc = next_loc
        else:
            direction = instructions[0]
            instructions = instructions[1:]
            # print(f'direction:{direction}', end=', ')
            cur_direction = rotate(cur_direction, direction)
    return 1000 * (cur_loc[1] + 1) + 4 * (cur_loc[0] + 1) + {(0, 1): 1, (0, -1): 3, (1, 0): 0, (-1, 0): 2}[cur_direction]


demo_input = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".split('\n')


def test_demo_input_part1():
    print()
    assert solution([l for l in demo_input]) == 6032

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

# def test_demo_input_part2():
#     print()
#     assert solution([l for l in demo_input], part=2) == 1623178306
#
# def test_part_2():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')


