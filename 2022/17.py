# solution to https://adventofcode.com/2022/day/17
from collections import defaultdict
from typing import List

aoc_day_number = '17'

def rock_generator():
    # rocklist = [['####'], ['.#.', '###', '.#.'], ['..#', '..#', '###'], ['#', '#', '#', '#'], ['##', '##']]
    # each rock specified as list of a str per column bottom to top, list runs from left to right
    rocklist = [['#', '#', '#', '#'], ['.#.', '###', '.#.'], ['#..', '#..', '###'], ['####'], ['##', '##']]
    while True:
        for ndx in range(5):
            yield (ndx, [[c == '#' for c in line] for line in rocklist[ndx]])

class Tunnel():
    def __init__(self):
        self.cols = [[False for c in range(20000000)] for _ in range(7)]
        self.top_filled = -1

    def get_top(self):
        return self.top_filled

    def fits(self, rock, location):
        for x in range(len(rock)):
            for y in range(len(rock[0])):
                if rock[x][y] and self.cols[x + location[0]][y + location[1]]:
                    return False
        return True


    def set_rock(self, rock, location):
        for x in range(len(rock)):
            for y in range(len(rock[0])):
                self.cols[x + location[0]][(y_value := y + location[1])] |= (pixel_set := rock[x][y])
                if pixel_set:
                    self.top_filled = max(self.top_filled, y_value)


def jet_generator(param):
    while True:
        for ndx, c in enumerate(param):
            yield (ndx, c)


def solution(scan_lines: List[str], part=1):
    print()
    gen = rock_generator()
    jet = jet_generator(scan_lines[0])
    t = Tunnel()
    print(f'top:{t.get_top()}')
    if part == 1:
        total_rocks = 2022
    else:
        total_rocks = (len(scan_lines[0] * 5))     # result: 308
        total_rocks = 1000000
    print(f'total_rocks:{total_rocks}   repeat_dist:{(len(scan_lines[0] * 5))}')

# 1000000000000
# 1514285714288

    print(f'part_2_guess: {(1000000000000 // 200) * 308}')
    stats = defaultdict(list)
    for _ in range(total_rocks):
        rock_ndx, rock = next(gen)
        x = 2
        y = t.get_top() + 4
        rock_moving = True
        first_move = True
        while rock_moving:
            jet_ndx, direction = next(jet)
            if first_move:
                first_move = False
                stats[jet_ndx].append((_, rock_ndx, t.get_top()))
            if direction == '>' and x < (7 - len(rock)) and t.fits(rock, (x+1, y)):
                x += 1
            elif direction == '<' and x > 0 and t.fits(rock, (x-1, y)):
                x -= 1
            if y > 0 and t.fits(rock, (x,y-1)):
                y -= 1
            else:
                t.set_rock(rock, (x,y))
                rock_moving = False
    print(f'recorded stats: {stats}')
    return t.get_top() + 1 + ((1000000000000 - 1000000) * (53 / 35))

demo_input = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""".split('\n')

# def test_demo_input_part1():
#     assert solution([l for l in demo_input]) == 3068
#
# def test_part_1():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

# def test_demo_input_part2():
#     assert solution([l for l in demo_input], part=2) == 3068

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')



# 1514285714288
# 1514285714291

# 1514285714982 is too low for part 2
