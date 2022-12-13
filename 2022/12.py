# solution to https://adventofcode.com/2022/day/12
from math import sqrt, ceil
import logging as log
from typing import List, Tuple

aoc_day_number = '12'

def part_1(height_map: List[str]):
    def neighbours(coordinate: Tuple[int, int], width, height):
        x, y = coordinate
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (nx := x + dx) >= 0 and nx < width and (ny := y + dy) >= 0 and ny < height:
                yield (nx, ny)

    width, height = (len(height_map[0]), len(height_map))
    sur_area = {(x,y):ord(h)  for y, line in enumerate(height_map) for x, h in enumerate(list(line))}
    start = target = None
    for k, v in sur_area.items():
        if v == ord('S'):
            start = k
            sur_area[start] = ord('a')
        elif v == ord('E'):
            target = k
            sur_area[target] = ord('z')

    seen = {}
    to_visit = [(start, 0)]
    shortest = width * height * 2
    while to_visit:
        visit, steps = to_visit.pop(0)
        if visit == target:
            shortest = min(shortest, steps)
        else:
            if visit not in seen or (visit in seen and steps < seen[visit]):
                seen[visit] = steps
                for n in neighbours(visit, width, height):
                    if sur_area[n] <= sur_area[visit] + 1:
                        to_visit.append((n, steps + 1))
    return shortest


def shortest_path(sur_area, width, height, start, target):
    def neighbours(coordinate: Tuple[int, int], width, height):
        x, y = coordinate
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (nx := x + dx) >= 0 and nx < width and (ny := y + dy) >= 0 and ny < height:
                yield (nx, ny)

    seen = {}
    to_visit = [(start, 0)]
    shortest = width * height * 2
    while to_visit:
        visit, steps = to_visit.pop(0)
        if visit == target:
            shortest = min(shortest, steps)
        else:
            if visit not in seen or (visit in seen and steps < seen[visit]):
                seen[visit] = steps
                for n in neighbours(visit, width, height):
                    if sur_area[n] <= sur_area[visit] + 1:
                        to_visit.append((n, steps + 1))
    return shortest


def part_2(height_map: List[str]):
    sur_area = {(x,y):ord(h)  for y, line in enumerate(height_map) for x, h in enumerate(list(line))}
    width, height = (len(height_map[0]), len(height_map))
    shortest = width * height * 2
    for k, v in sur_area.items():
        if v == ord('S'):
            sur_area[k] = ord('a')
        elif v == ord('E'):
            target = k
            sur_area[k] = ord('z')
    for k, v in sur_area.items():
        if sur_area[k] == ord('a'):
            shortest = min(shortest, shortest_path(sur_area, width, height, k, target))
    return shortest


def test_demo_input_part1():
    lines = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split('\n')
    assert part_1([l for l in lines]) == 31


def test_demo_input_part2():
    lines = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split('\n')
    assert part_2([l for l in lines]) == 29



def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {part_1(lines)}', end='')

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {part_2(lines)}', end='')

