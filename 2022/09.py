# solution to https://adventofcode.com/2022/day/5

from math import sqrt, ceil


class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, P):
            return self.x == other.x and self.y == other.y
        return False

    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def tup(self):
        return self.x, self.y

    def __repr__(self):
        return f"({self.x},{self.y})"


aoc_day_number = '09'


def solution(lines):
    initial = head = tail = P(0, 0)
    tail_visited = set()
    vectors = {'U': P(0, 1), 'D': P(0, -1), 'L': P(-1, 0), 'R': P(1, 0)}
    for line in lines:
        move, dist = line.split(' ')
        dist = int(dist)
        for steps in range(dist):
            head += vectors[move]
            if (cur_dist := (head - tail).length()) > sqrt(2):
                if head.y != tail.y:
                    tail.y += 1 if head.y - tail.y > 0 else -1
                if head.x != tail.x:
                    tail.x += 1 if head.x - tail.x > 0 else -1
            # print(f'{head}-{tail}  ', end='')
            tail_visited.add((tail.x, tail.y))
        # print()
    # print()
    # for y in reversed(range(7)):
    #     for x in range(7):
    #         if (x, y) in tail_visited:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    return len(tail_visited)


def part_2(lines):
    knots = [P(0, 0) for _ in range(10)]
    tail_visited = set()
    vectors = {'U': P(0, 1), 'D': P(0, -1), 'L': P(-1, 0), 'R': P(1, 0)}
    # print()
    for line in lines:
        move, dist = line.split(' ')
        dist = int(dist)
        for steps in range(dist):
            knots[0] += vectors[move]
            for ndx in range(1, len(knots)):
                head, tail = ndx - 1, ndx
                if (cur_dist := (knots[head] - knots[tail]).length()) > sqrt(2):
                    # print(f'dist {cur_dist} head:{knots[head]} tail:{knots[tail]}')
                    if knots[head].y != knots[tail].y:
                        knots[tail].y += 1 if knots[head].y - knots[tail].y > 0 else -1
                    if knots[head].x != knots[tail].x:
                        knots[tail].x += 1 if knots[head].x - knots[tail].x > 0 else -1
                if ndx == len(knots) - 1:
                    tail_visited.add((knots[-1].x, knots[-1].y))
            # for k in range(10):
            #     print(f'{knots[k]} ', end='')
            # print()
        # print()
    # print()
    # for y in reversed(range(7)):
    #     for x in range(7):
    #         if (x, y) in tail_visited:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    return len(tail_visited)


lines = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split('\n')


def test_demo_input():
    global  lines
    assert solution([l for l in lines]) == 13

def test_p2_first():
    global lines
    assert part_2([l for l in lines]) == 1

def test_p2_second():
    longer = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split('\n')
    assert part_2(longer) == 36


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')


def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {part_2(lines)}', end='')
