import collections
import math
from collections import defaultdict
from typing import List
import re

def sol_part1(lines: List[str], part = 1) -> int:
    total_worth = 0
    for line in lines:
        _, line = line.split(': ')
        left, right = line.split(' | ')
        left_set = set([int(p) for p in left.split()])
        right_set = set([int(p) for p in right.split()])
        winners = list(w for w in right_set if w in left_set)
        if winners:
            total_worth += math.pow(2, len(winners)-1)
    return int(total_worth)

def sol_part2(lines):
    card_count = collections.defaultdict(lambda: 1)
    for card_no, line in enumerate(lines, start=1):
        _, line = line.split(': ')
        left, right = line.split(' | ')
        left_set = set([int(p) for p in left.split()])
        right_set = set([int(p) for p in right.split()])
        winners = list(w for w in right_set if w in left_set)
        if winners:
            for next_card in range(card_no + 1, card_no + 1 + len(winners)):
                card_count[next_card] += card_count[card_no]
    return sum((card_count[x] for x in range(1, len(lines) + 1)))


def test_01():
    lines = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""[1:-1].split('\n')
    assert sol_part1(lines) == 13

def test_02():
    lines = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""[1:-1].split('\n')
    assert sol_part2(lines) == 30


if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day 01 part 1:{sol_part1(lines)}')
    print(f'day 01 part 2:{sol_part2(lines)}')


