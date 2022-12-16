# solution to https://adventofcode.com/2022/day/15
from collections import defaultdict
from functools import cmp_to_key
from math import sqrt, ceil
import logging as log
from typing import List, Tuple
from bitarray import bitarray

aoc_day_number = '15'

# https://pypi.org/project/bitarray/
# needed this damned thing to install first, so that pip could c++ compile it:
# https://learn.microsoft.com/en-us/visualstudio/releasenotes/vs2017-relnotes#15.9.51

def man_dist(s: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(s[0]-b[0]) + abs(s[1] - b[1])

def manhattan_borderpoints(centre: Tuple[int, int], dist: int):
    x, y = centre
    # print(f'generating points for {centre} dist:{dist}')
    for step in range(dist):
        yield (x - dist + step, y - step)
    for step in range(dist):
        yield (x + step, y - dist + step)
    for step in range(dist):
        yield (x + dist - step, y + step)
    for step in range(dist):
        yield (x - step, y + dist - step)


def solution(sensors: List[str], line_at=10, part=1):
    no_beacon_at = set()
    s_b_pairs = []
    beacons = []
    actual_sensors = []
    for sensor_line in sensors:
        parts = sensor_line.split(' ')
        s_x = int(parts[2][2:-1])
        s_y = int(parts[3][2:-1])
        s = (s_x, s_y)
        b_x = int(parts[-2][2:-1])
        b_y = int(parts[-1][2:])
        b = (b_x, b_y)
        s_b_pairs.append((s, b))
        beacons.append(b)
        actual_sensors.append(s)
        # print(f'{s} has man_dist {man_dist(s, b)}')

    if part ==1:
        for s, b in s_b_pairs:
            if abs(s[1] - line_at) <= man_dist(s, b):
                left_right_dist = abs(man_dist(s, b) - abs(s[1] - line_at))
                for x in range(s[0] - left_right_dist, s[0] + left_right_dist + 1):
                    if (x, line_at) not in beacons:
                        no_beacon_at.add((x, line_at))
        return len(no_beacon_at)
    else:
        # print(list(manhattan_borderpoints((8,7), man_dist((8, 7), (2, 10)) + 1)))
        candidates = defaultdict(int)
        for sensor, beacon in s_b_pairs:
            # print(f'finding points for {sensor} {beacon}')
            num_border_points = 0
            for point in manhattan_borderpoints(sensor, man_dist(sensor, beacon) + 1):
                candidates[point] += 1
                num_border_points += 1
            # print(f'sensor:{sensor} beacon:{beacon} man_dist:{man_dist(sensor, beacon)} adds {num_border_points} points')
        # print(f'list now has {len(candidates)} points')
        x = ((candidates[p], p) for p in candidates if p[0] >= 0 and p[1] <= 4000000)
        must_be_it =  sorted(list(x), reverse=True)[0][1]
        return 4000000 * must_be_it[0] + must_be_it[1]


def test_demo_input_part1():
    lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split('\n')
    assert solution([l for l in lines]) == 26


def test_demo_input_part2():
    lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split('\n')
    assert solution([l for l in lines], part=2) == 56000011


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines, line_at=2000000)}', end='')

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')

    # 11557863040754

