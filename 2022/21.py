# solution to https://adventofcode.com/2022/day/21
import copy
from collections import defaultdict, namedtuple
from typing import List
import re

aoc_day_number = '21'


def parse(tree: dict, node: str) -> int:
    if type(tree[node]) == int:
        return tree[node]
    else:
        oprnd_left, operator, oprnd_right = tree[node].split(' ')
        left = parse(tree, oprnd_left)
        right = parse(tree, oprnd_right)
        if operator == '+':
            return left + right
        elif operator == '*':
            return left * right
        elif operator == '-':
            return left - right
        else:
            return left // right


def contains_humn(tree, node):
    if type(tree[node]) == str:
        left, _, right = tree[node].split(' ')
        return contains_humn(tree, left) or contains_humn(tree, right)
    return node == 'humn'


def must_simplify(tree, node):
    pass


def simplify(tree, node, right_hand_value):
    if type(tree[node]) == str:
        oprnd_left, operator, oprnd_right = tree[node].split(' ')
        if contains_humn(tree, oprnd_left):
            right = parse(tree, oprnd_right)
            if operator == '+':
                right_hand_value -= right
                return simplify(tree, oprnd_left, right_hand_value)
            elif operator == '*':
                right_hand_value /= right
                return simplify(tree, oprnd_left, right_hand_value)
            elif operator == '-':
                right_hand_value += right
                return simplify(tree, oprnd_left, right_hand_value)
            else:
                right_hand_value *= right
                return simplify(tree, oprnd_left, right_hand_value)
        else:
            left = parse(tree, oprnd_left)
            if operator == '+':
                right_hand_value -= left
                return simplify(tree, oprnd_right, right_hand_value)
            elif operator == '*':
                right_hand_value /= left
                return simplify(tree, oprnd_right, right_hand_value)
            elif operator == '-':
                right_hand_value = left - right_hand_value
                return simplify(tree, oprnd_right, right_hand_value)
            else:
                right_hand_value = left / right_hand_value
                return simplify(tree, oprnd_right, right_hand_value)
    else:
        return right_hand_value

def solution(lines: List[str], part=1):
    tree = dict()
    for line in lines:
        left, right = line.split(': ')
        if right.isdigit():
            tree[left] = int(right)
        else:
            tree[left] = right
    if part == 1:
        return parse(tree, 'root')
    else:
        left, _, right = tree['root'].split(' ')
        # print(f'left:{left} {contains_humn(tree, left)}')
        # print(f'left:{right} {contains_humn(tree, right)}')
        if contains_humn(tree, right):
            left, right = right, left
        right_hand_value = parse(tree, right)
        # print(f'right_hand_value:{right_hand_value}')
        right_hand_value = simplify(tree, left, right_hand_value)
        return int(right_hand_value)


demo_input = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".split('\n')


def test_demo_input_part1():
    print()
    assert solution([l for l in demo_input]) == 152

def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

def test_demo_input_part2():
    print()
    assert solution([l for l in demo_input], part=2) == 301

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')


