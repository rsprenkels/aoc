# solution to https://adventofcode.com/2022/day/13
from functools import cmp_to_key
from math import sqrt, ceil
import logging as log
from typing import List, Tuple

aoc_day_number = '13'

def compare(p1, p2):
    if type(p1) is int and type(p2) is int:
        if p1 < p2:
            return -1  # 'right'
        elif p1 > p2:
            return 1   # 'wrong'
        else:
            return 0   # 'equal'
    elif type(p1) is list and type(p2) is list:
        for a, b in zip(p1, p2):
            res = compare(a, b)
            if res != 0:
                return res
        if len(p1) < len(p2):
            return -1
        elif len(p1) > len(p2):
            return 1
        else:
            return 0
    else:
        if type(p1) is int:
            return compare([p1], p2)
        else:
            return compare(p1, [p2])


def part_1(packets: List[str]):
    pair_list = []
    while packets:
        pair = (eval(packets.pop(0)), eval(packets.pop(0)))
        pair_list.append(pair)
        if packets:
            packets.pop(0)
    return sum((ndx + 1 for ndx, pair in enumerate(pair_list) if compare(*pair) < 0))


def part_2(packets: List[str]):
    packet_list = []
    packets.append('[[2]]')
    packets.append('[[6]]')
    for packet in packets:
        if packet != '':
            packet_list.append(eval(packet))
    packet_list.sort(key=cmp_to_key(compare))
    for ndx, p in enumerate(packet_list):
        if p == eval('[[2]]'):
            a = ndx + 1
        if p == eval('[[6]]'):
            b = ndx + 1
    return a * b


def test_demo_input_part1():
    lines = list(open(f'{aoc_day_number}_demo.txt').read().splitlines())
    assert part_1([l for l in lines]) == 13


def test_demo_input_part2():
    lines = list(open(f'{aoc_day_number}_demo.txt').read().splitlines())
    assert part_2([l for l in lines]) == 140


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {part_1(lines)}', end='')

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {part_2(lines)}', end='')

