# solution to https://adventofcode.com/2022/day/18
from collections import defaultdict
from typing import List

aoc_day_number = '18'


def around(cube):
    x, y, z = cube
    yield (x-1, y, z)
    yield (x+1, y, z)
    yield (x, y+1, z)
    yield (x, y-1, z)
    yield (x, y, z+1)
    yield (x, y, z-1)


def reachable(cubes, cube, direction):
    while min(cube) > 0 and max(cube) < 25:
        cube = tuple((x + y for x,y in zip(cube, direction)))
        if cube in cubes:
            return False
    return True


def can_get_out_via(cubes, a):
    directions = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
    queue = [a]
    seen = set()
    while queue:
        via = queue.pop()
        seen.add(via)
        if min(via) <= 0 or max(via) >= 25:
            return True
        else:
            for a in (a for a in around(via) if a not in seen and a not in cubes):
                queue.append(a)
    return False


def solution(lines: List[str], part=1):
    cubes = set([tuple(map(int, line.split(','))) for line in lines])
    surface = 0
    if part == 1:
        for cube in cubes:
            surface += sum(1 for a in around(cube) if a not in cubes)
    else:
        directions = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
        for cube in cubes:
            for a in around(cube):
                if a not in cubes:
                    if can_get_out_via(cubes, a):
                        surface += 1
    return surface


demo_input = """1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,2
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".split('\n')

def test_demo_input_part1():
    assert solution([l for l in demo_input]) == 64

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

def test_demo_input_part2():
    assert solution([l for l in demo_input], part=2) == 58

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')
