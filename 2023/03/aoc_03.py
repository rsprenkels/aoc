from collections import defaultdict
from typing import List
import re



def sol_part1(lines: List[str], part = 1) -> int:
    def search_symbol(lines, x_range=(0,0), y_par=0):
        def box_generator(xmin, xmax, y_par, w=len(lines[0]), h=len(lines)):
            for x in range(xmin - 1, xmax + 1):
                for y in [y_par-1, y_par+1]:
                    if x >= 0 and x < w and y >= 0 and y < h:
                        yield (x,y)
            if xmin-1 >= 0:
                yield (xmin-1, y_par)
            if xmax < w:
                yield (xmax, y_par)

        xmin, xmax = x_range
        for x,y in box_generator(xmin, xmax, y_par):
            print(f'for xmin={xmin} xmax={xmax} y_par={y_par} checking {x},{y}')
            if (symbol := lines[y][x]) != '.' and not symbol.isdigit():
                return (True, symbol, (x,y))
        return (False, None, None)

    sum_partnumbers = 0
    star_numbers = defaultdict(list)
    for y, line in enumerate(lines):
        x = 0
        while x < len(line):
            while x < len(line) and (not line[x].isdigit()):
                x += 1
            if x < len(line):
                start = x
                while x < len(line) and line[x].isdigit():
                    x += 1
                number = int(line[start:x])
                print(f'found {number} at y={y} x=[{start}:{x}]')
                has_symbol, the_symbol, location = search_symbol(lines, x_range=(start, x), y_par=y)
                if has_symbol:
                    sum_partnumbers += number
                    if the_symbol == '*':
                        star_numbers[location].append(number)
                else:
                    print(f'{number} does not count')
    if part == 1:
        return sum_partnumbers
    else:
        return sum([star_numbers[k][0] * star_numbers[k][1] for k in list(star_numbers.keys()) if len(star_numbers[k]) == 2])

def sol_part2(lines):
    return sol_part1(lines, part=2)


def test_01():
    lines = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""[1:-1].split('\n')
    assert sol_part1(lines) == 4361

def test_02():
    lines = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""[1:-1].split('\n')
    assert sol_part2(lines) == 467835



if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day 01 part 1:{sol_part1(lines)}')
    print(f'day 01 part 2:{sol_part2(lines)}')


