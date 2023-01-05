# solution to https://adventofcode.com/2022/day/24
import copy
from collections import defaultdict, namedtuple
from functools import cmp_to_key
from typing import List
import re
from dataclasses import dataclass

aoc_day_number = '24'

@dataclass(frozen=True)
class P:
    x: int
    y: int

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)


@dataclass
class Blizzard:
    loc : P
    direction : str


def show_tiles(tiles, w, h):
    for y in range(h):
        for x in range(w):
            tiles_here = list(t for t in tiles if t.loc == P(x, y))
            if len(tiles_here) > 1:
                c = str(len(tiles_here))[0]
            elif len(tiles_here) == 1:
                c = tiles_here[0].direction
            else:
                c = '.'
            print(c, end='')
        print()
    print()

def get_tiles_at(target_time, tiles_in_time, w, h):
    def get_next(tiles: List[Blizzard], w, h) -> List[Blizzard]:
        new_tiles = []
        for b in tiles:
            x = b.loc.x
            y = b.loc.y
            if b.direction == '>':
                x = x + 1 if x < w - 2 else 1
                new_tiles.append(Blizzard(P(x, y), b.direction))
            elif b.direction == '<':
                x = x - 1 if x > 1 else w - 2
                new_tiles.append(Blizzard(P(x, y), b.direction))
            elif b.direction == '^':
                y = y - 1 if y > 1 else h - 2
                new_tiles.append(Blizzard(P(x, y), b.direction))
            elif b.direction == 'v':
                y = y + 1 if y < h - 2 else 1
                new_tiles.append(Blizzard(P(x, y), b.direction))
            else:
                raise Exception('get_tiles_at exception')
        return new_tiles

    if target_time not in tiles_in_time:
        tiles_in_time[target_time] = get_next(tiles_in_time[target_time - 1], w, h)
    return tiles_in_time[target_time]


def pos_moves(loc, w, h, start, finish):
    yield loc
    if loc.x >= 2 and loc.y > 0:
        yield loc - P(1, 0)
    if loc.x < w - 2 and loc.y > 0:
        yield loc + P(1, 0)
    if loc.y >= 2 or loc - P(0, 1) == start:
        yield loc - P(0, 1)
    if loc.y < h - 2 or loc + P(0, 1) == finish:
        yield loc + P(0, 1)


def solution(lines: List[str], part=1):
    tiles_in_time = {}
    t0 = []
    start = finish = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in '<>^v':
                t0.append(Blizzard(loc=P(x, y), direction=c))
            if y == 0 and c == '.':
                start = P(x, 0)
            if y == len(lines) - 1 and c == '.':
                finish = P(x, len(lines) - 1)
    w = len(lines[0])
    h = len(lines)
    tiles_in_time[0] = t0
    queue = [(0, start)]
    show_tiles(tiles_in_time[0], w, h)
    shortest_time = 100 ** 10
    seen = set()
    while queue:
        closest_dist = 100 ** 10
        closest_ndx = 0
        # for ndx, e in enumerate(queue):
        #     if (man_dist := (abs(e[1].x - finish.x) + abs(e[1].y - finish.y))) < closest_dist:
        #         closest_dist = man_dist
        #         closest_ndx = ndx
        minute, location = queue.pop(closest_ndx)
        if location == finish:
            shortest_time = min(shortest_time, minute)
        elif minute < shortest_time and (minute, location) not in seen:
            seen.add((minute, location))
            tx = get_tiles_at(minute + 1, tiles_in_time, w, h)
            possible_nxt_locs = list(x for x in pos_moves(location, w, h, start, finish) if x not in (t.loc for t in tx))
            for pn in possible_nxt_locs:
                queue.append((minute + 1, pn))
            # show_tiles(tx, w, h)
    return shortest_time

demo_input = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".split('\n')


def test_demo_input_part1():
    print()
    result= solution([l for l in demo_input])
    assert result == 18

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

# def test_demo_input_part2():
#     print()
#     assert solution([l for l in demo_input], part=2) == 5031

# def test_part_2():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')


