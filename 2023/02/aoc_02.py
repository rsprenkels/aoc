from typing import List
import re

def sol_part1(lines: List[str], part = 1) -> int:

    total_power = 0
    total = 0
    for line in lines:
        max_per_color = {'red':0, 'green':0, 'blue':0}
        game, reveals = line.split(': ')
        game_id = int(game[5:])
        for reveal in reveals.split('; '):
            for ball in reveal.split(', '):
                number, color = list(ball.split(' '))
                max_per_color[color] = max(max_per_color[color], int(number))
        if max_per_color['red'] > 12 or max_per_color['green'] > 13 or max_per_color['blue'] > 14:
            pass
        else:
            total += game_id
        total_power += max_per_color['red'] * max_per_color['green'] * max_per_color['blue']
    if part == 1:
        return total
    else:
        return total_power


def sol_part2(lines):
    return sol_part1(lines, part=2)


def test_01():
    lines = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""[1:-1].split('\n')
    assert sol_part1(lines) == 8

def test_02():
    lines = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""[1:-1].split('\n')
    assert sol_part2(lines) == 2286



if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day 01 part 1:{sol_part1(lines)}')
    print(f'day 01 part 2:{sol_part2(lines)}')


