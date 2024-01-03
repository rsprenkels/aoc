import collections
import locale
import math
from collections import defaultdict
from functools import cache, cmp_to_key
from typing import List
import re

day_number = '07'

def cmp_hands_p1(a, b):
    frequencies = []
    for hand in (a, b):
        freq = defaultdict(int)
        cards, value = hand
        for c in cards:
            freq[c] += 1
        frequencies.append(tuple(sorted(freq.values(), reverse=True)))
    if frequencies[0] < frequencies[1]:
        return -1
    elif frequencies[0] > frequencies[1]:
        return 1
    else:
        for c1, c2 in zip(a[0], b[0]):
            if c1 != c2:
                return 'AKQJT98765432'.find(c2) - 'AKQJT98765432'.find(c1)
        return 0

def cmp_hands_p2(a, b):
    frequencies = []
    for hand in (a, b):
        freq = defaultdict(int)
        cards, value = hand
        jokers = 0
        for c in cards:
            if c == 'J':
                jokers += 1
            else:
                freq[c] += 1
        values = sorted(freq.values(), reverse=True)
        if values:
            values[0] += jokers
        else:
            values = [jokers]
        frequencies.append(tuple(values))
    if frequencies[0] < frequencies[1]:
        return -1
    elif frequencies[0] > frequencies[1]:
        return 1
    else:
        for c1, c2 in zip(a[0], b[0]):
            if c1 != c2:
                return 'AKQT98765432J'.find(c2) - 'AKQT98765432J'.find(c1)
        return 0


def sol_part1(lines: List[str], part = 1) -> int:
    hands = list(tuple(line.split()) for line in lines)
    cmp_fuction = [cmp_hands_p1, cmp_hands_p2][part != 1]
    sorted_hands = sorted(hands, key=cmp_to_key(cmp_fuction))
    return sum(list(int(hand[1]) * rank for rank, hand in enumerate(sorted_hands, start=1)))

def sol_part2(lines):
    return sol_part1(lines, part=2)

lines = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""[1:-1].split('\n')

def test_cmp_a():
    c1, c2 = ('QQQJA', 483), ('T55J5', 684)
    assert cmp_hands_p1(c1, c2) > 0
    assert cmp_hands_p1(c2, c1) < 0
    assert cmp_hands_p1(c1, c1) == 0
    assert cmp_hands_p1(c2, c2) == 0

def test_01():
    assert sol_part1(lines) == 6440

def test_02():
    assert sol_part2(lines) == 5905

if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day {day_number} part 1:{sol_part1(lines)}')
    print(f'day {day_number} part 2:{sol_part2(lines)}')


