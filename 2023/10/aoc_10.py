import collections
import itertools
import locale
import math
from collections import defaultdict
from functools import cache, cmp_to_key
from typing import List
import re

day_number = '10'


def p_add(point, direction):
    dir = {'N':(0,-1), 'E':(1,0), 'S':(0,1), 'W':(-1,0)}[direction]
    return (point[0] + dir[0], point[1] + dir[1])


def sol_part1(lines: List[str], part = 1) -> int:
    def is_valid_gridpoint(a):
        x,y = a
        return x >=0 and x < len(lines[0]) and y >=0 and y < len(lines)
    grid = {(x,y):c for y,line in enumerate(lines) for x,c in enumerate(line)}
    start = [k for k,v in grid.items() if v == 'S'][0]
    # find a valid starting direction, and what the S symbol must be
    connected = ''
    direction = ''
    for search_direction in list("NESW"):
        if is_valid_gridpoint(look_at := p_add(start, search_direction)):
            if search_direction == 'N' and grid[look_at] in '|7F':
                connected += 'N'
                direction = 'N'
            elif search_direction == 'E' and grid[look_at] in '-J7':
                connected += 'E'
                direction = 'E'
            elif search_direction == 'S' and grid[look_at] in '|LJ':
                connected += 'S'
                direction = 'S'
            elif search_direction == 'W' and grid[look_at] in '-LF':
                connected += 'W'
                direction = 'W'
    connected = ''.join(sorted(list(connected)))
    grid[start] = {'SN':'|', 'EW':'-', 'EN':'L', 'ES':'F', 'SW':'7', 'NW':'J'}[connected]
    current_location = start
    seen = set()
    # one step in direction (0) finds a (1) so continue (2)
    rules = ['N|N','N7W','NFE','E-E','EJN','E7S','S|S','SLE','SJW','W-W','WLN','WFS']
    routing = {r[0:2]:r[2] for r in rules}
    while current_location not in seen:
        seen.add(current_location)
        current_location = p_add(current_location, direction)
        if grid[current_location] != 'S':
            direction = routing[direction + grid[current_location]]
    if part == 1:
        return len(seen) // 2
    print('printing the loop')
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x,y) in seen:
                print(grid[(x,y)], end='')
            else:
                print('.', end='')
        print()
    num_enclosed = 0
    for loc in ((x,y) for y in range(len(lines)) for x in range(len(lines[0]))):
        if loc not in seen:
            num_crossings = 0
            while is_valid_gridpoint((loc := p_add(loc, 'S'))):
                if loc in seen:
                    start_symbol = grid[loc]
                    if start_symbol == '-':
                        num_crossings += 1
                    else:
                        while grid[(loc := p_add(loc, 'S'))] == '|':
                            pass
                        end_symbol = grid[loc]
                        corners = start_symbol + end_symbol
                        if corners not in ['7J', 'FL']:
                            num_crossings += 1
            if num_crossings % 2 == 1:
                num_enclosed += 1
    return num_enclosed
    # 462 is too high -> needed to replace the S with its actual symbol


def sol_part2(lines):
    return sol_part1(lines, part=2)


def test_01():
    lines = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""[1:-1].split('\n')
    assert sol_part1(lines) == 8

def test_02():
    lines = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""[1:-1].split('\n')
    assert sol_part2(lines) == 10

if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day {day_number} part 1:{sol_part1(lines)}')
    print(f'day {day_number} part 2:{sol_part2(lines)}')


