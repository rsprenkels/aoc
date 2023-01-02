# solution to https://adventofcode.com/2022/day/23
import copy
from collections import defaultdict, namedtuple
from typing import List
import re
from dataclasses import dataclass

aoc_day_number = '23'

@dataclass(frozen=True)
class P:
    x: int
    y: int

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)


@dataclass
class Elf:
    loc: P
    proposed: P = None

    def find_proposed(self, locations, valid_directions):
        all_around_free = True
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x != 0 or y != 0) and P(self.loc.x + x, self.loc.y + y) in locations:
                    all_around_free = False
                    break
        if all_around_free:
            return None
        else:
            for d in valid_directions:
                if d == 'N':
                    if all(self.loc + offset not in locations for offset in (P(-1, -1), P(0, -1), P(1, -1))):
                        return self.loc + P(0, -1)
                elif d == 'S':
                    if all(self.loc + offset not in locations for offset in (P(-1, 1), P(0, 1), P(1, 1))):
                        return self.loc + P(0, 1)
                elif d == 'E':
                    if all(self.loc + offset not in locations for offset in (P(1, -1), P(1, 0), P(1, 1))):
                        return self.loc + P(1, 0)
                else:
                    if all(self.loc + offset not in locations for offset in (P(-1, -1), P(-1, 0), P(-1, 1))):
                        return self.loc + P(-1, 0)


def solution(lines: List[str], part=1):
    valid_directions = list("NSWE")
    elves = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                elves.append(Elf(loc=P(x, y)))
    elves_have_moved = True
    round_counter = 0
    while elves_have_moved and ((part == 1 and round_counter < 10) or part == 2):
        # show(elves, round_counter)
        round_counter += 1
        locations = set(e.loc for e in elves)
        wanted_as_target = defaultdict(int)
        for elf in elves:
            elf.proposed = (target_location := elf.find_proposed(locations, valid_directions))
            wanted_as_target[target_location] += 1
        elves_have_moved = False
        for elf in (elf for elf in elves if wanted_as_target[elf.proposed] == 1):
            elves_have_moved = True
            elf.loc = elf.proposed
        first = valid_directions.pop(0)
        valid_directions.append(first)
    show(elves, round_counter)
    locs = list(e.loc for e in elves)
    width = max(loc.x for loc in locs) - min(loc.x for loc in locs) + 1
    height = max(loc.y for loc in locs) - min(loc.y for loc in locs) + 1
    return round_counter, width * height - len(elves)


def show(elves, round_counter):
    print(f'\n\nround: {round_counter}')
    xy = set(e.loc for e in elves)
    for y in range(-2, 10):
        for x in range(-3, 10):
            if P(x, y) in (e.loc for e in elves):
                print('#', end='')
            else:
                print('.', end='')
        print()


demo_input = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""".split('\n')


def test_demo_input_part1():
    print()
    round_number, area = solution([l for l in demo_input])
    assert area == 110

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

# def test_demo_input_part2():
#     print()
#     assert solution([l for l in demo_input], part=2) == 5031

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')


