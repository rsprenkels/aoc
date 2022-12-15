# solution to https://adventofcode.com/2022/day/15
from functools import cmp_to_key
from math import sqrt, ceil
import logging as log
from typing import List, Tuple

aoc_day_number = '15'

# https://pypi.org/project/bitarray/

def man_dist(s: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(s[0]-b[0]) + abs(s[1] - b[1])


def solution(sensors: List[str], line_at=10):
    no_beacon_at = set()
    s_b_pairs = []
    beacons = []
    actual_sensors = []
    for s in sensors:
        parts = s.split(' ')
        s_x = int(parts[2][2:-1])
        s_y = int(parts[3][2:-1])
        b_x = int(parts[-2][2:-1])
        b_y = int(parts[-1][2:])
        s_b_pairs.append(((s_x, s_y), (b_x, b_y)))
        beacons.append((b_x, b_y))
        actual_sensors.append((s_x, s_y))
    for s, b in s_b_pairs:
        if abs(s[1] - line_at) <= man_dist(s, b):
            left_right_dist = abs(man_dist(s, b) - abs(s[1] - line_at))
            for x in range(s[0] - left_right_dist, s[0] + left_right_dist + 1):
                if (x, line_at) not in beacons:
                    no_beacon_at.add((x, line_at))
    return len(no_beacon_at)

#
# def test_demo_input_part1():
#     lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split('\n')
#     assert solution([l for l in lines]) == 26


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines, line_at=2000000)}', end='')
