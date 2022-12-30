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


def get_next_loc(loc, direction, map):
    # print('1', end='')
    cur_x, cur_y = loc
    next_loc = tuple(a + b for a, b in zip(loc, direction))
    if next_loc in map:
        return next_loc, direction
    else:
        if direction == (1, 0):
            return (min(x for x,y in map if y == cur_y), cur_y), direction
        elif direction == (-1, 0):
            return (max(x for x,y in map if y == cur_y), cur_y), direction
        elif direction == (0, 1):
            return (cur_x, min(y for x,y in map if x == cur_x)), direction
        elif direction == (0, -1):
            return (cur_x, max(y for x,y in map if x == cur_x)), direction
        else:
            raise Exception('this should never happen')


# 111223 for part 2 still too low
# 129007 for part 2 still too low

def get_next_loc_part2(loc, direction, map, tile_size=50):
    # print('2', end='')
    cube = {}

    cube[((1, 0), (0, -1))] = ('swap', (1, 0), (-50, 150))  # A F
    cube[((0, 3), (-1, 0))] = ('swap', (0, 1), (50, -150))  # F A

    cube[((1, 0), (-1, 0))] = ('mir_x', (1, 0), (-50, 100))  # A D
    cube[((0, 2), (-1, 0))] = ('mir_x', (1, 0), (50, -100))   # D A

    cube[((2, 0), (1, 0))] = ('mir_x', (-1, 0), (-50, 100))  # B E
    cube[((1, 2), (1, 0))] = ('mir_x', (-1, 0), (50, -100))  # E B

    cube[((2, 0), (0, -1))] = ('', (0, -1), (-100, 199))  # B F
    cube[((0, 3), (0, 1))] = ('', (0, 1), (100, -199))    # F B

    cube[((2, 0), (0, 1))] = ('swap', (-1, 0), (-50, 50))  # B C
    cube[((1, 1), (1, 0))] = ('swap', (0, -1), (50, -50))    # C B

    cube[((1, 1), (-1, 0))] = ('swap', (0, 1), (-50, 50))   # C D
    cube[((0, 2), (0, -1))] = ('swap', (1, 0), (50, -50))   # D C

    cube[((1, 2), (0, 1))] = ('swap', (-1, 0), (-50, 50))  # E F
    cube[((0, 3), (1, 0))] = ('swap', (0, -1), (50, -50))    # F E

    cur_x, cur_y = loc
    next_loc = tuple(a + b for a, b in zip(loc, direction))
    if next_loc in map:
        return next_loc, direction
    else:
        tile = (cur_x // tile_size, cur_y // tile_size)
        action, new_dir, translate = cube[(tile, direction)]
        x, y = cur_x % 50, cur_y % 50
        if action == 'mir_x':
            y = 49 - y
        elif action == 'mir_y':
            x = 49 - x
        elif action == 'swap':
            x, y = y, x
        x += tile[0] * 50 + translate[0]
        y += tile[1] * 50 + translate[1]
        return (x, y), new_dir


def solution(lines: List[str], part=1, get_next_loc=get_next_loc):
    map = {}
    for y, line in enumerate(lines[:-2]):
        for x, c in enumerate(line):
            if c != ' ':
                map[(x, y)] = c
    if part == 2:
        get_next_loc = get_next_loc_part2
    cur_loc = (min(x for x, y in map if y == 0), 0)
    cur_direction = (1, 0)
    instructions = lines[-1]
    while instructions:
        if instructions[0].isdigit():
            dist = int((match := re.search(r'^\d+', instructions)).group())
            instructions = instructions[match.end():]
            # print(f'dist:{dist}', end=' ')
            for step in range(dist):
                next_loc, next_direction = get_next_loc(cur_loc, cur_direction, map)
                if map[next_loc] == '#':
                    break
                else:
                    cur_loc = next_loc
                    cur_direction = next_direction
        else:
            direction = instructions[0]
            instructions = instructions[1:]
            # print(f'direction:{direction}', end=', ')
            cur_direction = rotate(cur_direction, direction)
    print(f'ended at loc {cur_loc} in direction {cur_direction}')
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


# def test_demo_input_part1():
#     print()
#     assert solution([l for l in demo_input]) == 6032

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

# def test_nextloc():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     map = {}
#     for y, line in enumerate(lines[:-2]):
#         for x, c in enumerate(line):
#             if c != ' ':
#                 map[(x, y)] = c
#     assert get_next_loc_part2((148,0), (1, 0), map) == ((149, 0), (1, 0))
#     assert get_next_loc_part2((149,0), (1, 0), map) == ((99, 149), (-1, 0))
#     assert get_next_loc_part2((149,10), (1, 0), map) == ((99, 139), (-1, 0))
#
#     assert get_next_loc_part2((149,0), (0, -1), map) == ((49, 199), (0, -1))
#     assert get_next_loc_part2((49,199), (0, 1), map) == ((149, 0), (0, 1))

# def test_demo_input_part2():
#     print()
#     assert solution([l for l in demo_input], part=2) == 5031

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')


