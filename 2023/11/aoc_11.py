import collections
import itertools
import locale
import math
from collections import defaultdict
from functools import cache, cmp_to_key
from typing import List
import re

day_number = '11'

def sol_part1(lines: List[str], part = 1) -> int:
    grid = [[c for c in line] for line in lines]
    for row_ndx in range(len(grid)-1, -1, -1):
        if all(grid[row_ndx][x] == '.' for x in range(len(grid[0]))):
            grid.insert(row_ndx, ['.' for _ in range(len(grid[0]))])
    for col_ndx in range(len(grid[0])-1, -1, -1):
        if all(grid[y][col_ndx] == '.' for y in range(len(grid))):
            for row_ndx in range(len(grid)):
                grid[row_ndx].insert(col_ndx, '.')
    # print()
    # for y in range(len(grid)):
    #     print(''.join(grid[y]))
    galaxies = [(x,y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '#']
    total_dist = 0
    for a, b in itertools.combinations(galaxies, 2):
        total_dist += (abs(b[0] - a[0]) + abs(b[1] - a[1]))
    return total_dist

def sol_part2(lines, expansion=1000000):
    grid = [[c for c in line] for line in lines]
    empty_rows, empty_cols = ([], [])
    for row_ndx in range(len(grid)-1, -1, -1):
        if all(grid[row_ndx][x] == '.' for x in range(len(grid[0]))):
            empty_rows.append(row_ndx)
    for col_ndx in range(len(grid[0])-1, -1, -1):
        if all(grid[y][col_ndx] == '.' for y in range(len(grid))):
            empty_cols.append(col_ndx)
    galaxies = [(x,y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '#']
    total_dist = 0
    for a, b in itertools.combinations(galaxies, 2):
        total_dist += (abs(b[0] - a[0]) + abs(b[1] - a[1]))
        for x in range(min(a[0], b[0]), max(a[0], b[0])):
            if x in empty_cols:
                total_dist += (expansion - 1)
        for y in range(min(a[1], b[1]), max(a[1], b[1])):
            if y in empty_rows:
                total_dist += (expansion - 1)
    return total_dist

lines = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""[1:-1].split('\n')

def test_01():
    assert sol_part1(lines) == 374

def test_02():
    assert sol_part2(lines, expansion=100) == 8410

if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day {day_number} part 1:{sol_part1(lines)}')
    print(f'day {day_number} part 2:{sol_part2(lines)}')


