# solution to https://adventofcode.com/2022/day/14
from math import sqrt, ceil
import logging as log
from typing import List, Tuple

aoc_day_number = '14'


def drop_sand(cave, location, lowest_rock,  has_floor=False):
    if location in cave:
        return False
    else:
        # lowest_rock = max(point[1] for point in cave if cave[point] == '#')
        if has_floor:
            lowest_rock += 1
        x,y = location
        while y < lowest_rock:
            if (x, y+1) not in cave:
                y += 1
            elif (x-1, y+1) not in cave:
                x -= 1
                y += 1
            elif (x+1, y+1) not in cave:
                x += 1
                y += 1
            elif has_floor and y+1 == lowest_rock:
                break
            else:
                break
        if  y < lowest_rock or has_floor:
            cave[(x,y)] = 'o'
            return True
        else:
            return False


def solution(rock_paths: List[str], has_floor=False):
    cave = {}
    for points_list in (rock_path.split(' -> ') for rock_path in rock_paths):
        for p_from, p_to in zip(points_list, points_list[1:]):
            x_from, y_from = map(int, p_from.split(','))
            x_to, y_to = map(int, p_to.split(','))
            for x in range(min(x_from, x_to), max(x_from, x_to) + 1):
                for y in range(min(y_from, y_to), max(y_from, y_to) + 1):
                    cave[(x,y)] = '#'
    lowest_rock = max(point[1] for point in cave if cave[point] == '#')

    # draw_cave(cave)

    units_at_rest = 0
    while drop_sand(cave, (500,0), has_floor=has_floor, lowest_rock=lowest_rock):
        units_at_rest += 1
        # draw_cave(cave)
    return units_at_rest


def draw_cave(cave):
    print()
    for y in range(15):
        for x in range(490, 510):
            print(cave[(x, y)] if (x, y) in cave.keys() else '.', end='')
        print()


def test_demo_input_part1():
    lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split('\n')
    assert solution([l for l in lines]) == 24


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')


def test_demo_input_part2():
    lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split('\n')
    assert solution([l for l in lines], has_floor=True) == 93


def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, has_floor=True)}', end='')

