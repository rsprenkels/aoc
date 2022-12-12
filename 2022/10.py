# solution to https://adventofcode.com/2022/day/10
from math import sqrt, ceil
import logging as log

aoc_day_number = '10'

class CPU:
    def __init__(self):
        self.x_reg = 1
        self.cycle_count = 0
        self.sig_strength = []
        self.crt = [[' ' for _ in range(40)] for line in range(6)]

    def cycle(self, num_cycles: int):
        for _ in range(num_cycles):
            self.one_cycle()

    def one_cycle(self):
        col = self.cycle_count % 40
        row = self.cycle_count // 40
        # print(f'cyc:{self.cycle_count} row:{row} col:{col}')
        if col in range(self.x_reg - 1, self.x_reg+2):
            self.crt[row][col] = '#'
        else:
            self.crt[row][col] = '.'
        self.cycle_count += 1
        if (self.cycle_count + 20) % 40 == 0:
            # print(f'x:{self.x_reg} cc:{self.cycle_count}')
            self.sig_strength.append(self.x_reg * self.cycle_count)

    def execute(self, instruction: str):
        opcode = instruction[:4]
        if opcode == 'addx':
            self.cycle(2)
            value = int(instruction[5:])
            self.x_reg += value
            # print(f'{opcode} {value}')
        elif opcode == 'noop':
            self.cycle(1)
            # print(f'{opcode}')

def solution(instructions):
    cpu = CPU()

    for instruction in instructions:
        cpu.execute(instruction)
    print()
    for row in range(6):
        print(''.join(cpu.crt[row]))
    print()
    return sum(cpu.sig_strength[:6])

def test_demo_input():
    lines = list(open(f'{aoc_day_number}_demo.txt').read().splitlines())
    assert solution([line for line in lines]) == 13140


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')


def test_part_2():
    print(f' day {aoc_day_number} part 2: EKRHEPUZ', end='')
        ####.#..#.###..#..#.####.###..#..#.####.
        #....#.#..#..#.#..#.#....#..#.#..#....#.
        ###..##...#..#.####.###..#..#.#..#...#..
        #....#.#..###..#..#.#....###..#..#..#...
        #....#.#..#.#..#..#.#....#....#..#.#....
        ####.#..#.#..#.#..#.####.#.....##..####.


# def test_part_2():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 2: {part_2(lines)}', end='')

# EKRHEPUZ