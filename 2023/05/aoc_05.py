import collections
import math
from collections import defaultdict
from functools import cache
from typing import List
import re


def apply_map(m, seed):
    for map_line in m:
        dest, source, len = map_line
        if seed >= source and seed < source + len:
            return seed - source + dest
    return seed


def sol_part1(lines: List[str], part = 1) -> int:
    seeds = list(map(int, lines[0][7:].split()))
    mappings = []

    def apply_all_mappings(seed):
        for m in mappings:
            seed = apply_map(m, seed)
        return seed

    ndx = 3
    while ndx < len(lines):
        mappings.append((cur_mapping := []))
        while ndx < len(lines) and (line := lines[ndx]) != '':
            ndx += 1
            cur_mapping.append(tuple(map(int, line.split())))
        ndx += 2
    map_result = []
    if part == 1:
        for seed in seeds:
            result = apply_all_mappings(seed)
            map_result.append(result)
        return min(map_result)
    else:
        min_result = 99999999999999999999999999999999999999
        while seeds:
            start, length = seeds.pop(0), seeds.pop(0)
            print(f'checking all from {start:9} to {start + length:9}')
            for seed in range(start, start + length):
                result = apply_all_mappings(seed)
                min_result = min(result, min_result)
        return min_result



def sol_part2(lines):
    return sol_part1(lines, part=2)

lines = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""[1:-1].split('\n')


def test_01():
    assert sol_part1(lines) == 35

def test_02():
    assert sol_part2(lines) == 46


if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day 01 part 1:{sol_part1(lines)}')
    print(f'day 01 part 2:{sol_part2(lines)}')


