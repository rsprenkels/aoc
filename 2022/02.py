# solution to https://adventofcode.com/2022/day/2

def total_score(lines):
    total_score = 0
    defeats = {'A':'Z', 'C':'Y', 'B':'X'}
    draw = {opponent:you for (opponent, you) in zip('ABC','XYZ')}
    points = {'X':1, 'Y':2, 'Z':3}
    for line in lines:
        game_score = 0
        (opponent, you) = line.split(' ')
        if draw[opponent] == you:
            game_score += 3
        elif defeats[opponent] != you:
             game_score += 6
        game_score += points[you]
        total_score += game_score
    return total_score


def must_end_like(lines):
    total_score = 0
    loses_from = {'A':'Y', 'C':'X', 'B':'Z'}
    defeats = {'A':'Z', 'C':'Y', 'B':'X'}
    draw = {opponent:you for (opponent, you) in zip('ABC','XYZ')}
    points = {'X':1, 'Y':2, 'Z':3}
    for line in lines:
        game_score = 0
        (opponent, you) = line.split(' ')
        if you == 'X': # opponent must win
            game_score += points[defeats[opponent]]
        elif you == 'Y': # must end in draw
            game_score += points[draw[opponent]] + 3
        else: # opponent must lose
            game_score += points[loses_from[opponent]] + 6
        total_score += game_score
    return total_score


def test_1():
    lines = """A Y
B X
C Z""".split('\n')

    assert total_score(lines) == 15

def test_1a():
    lines = """A Y
B X
C Z""".split('\n')

    assert must_end_like(lines) == 12


def test_2():
    lines = list(open('02.txt').read().splitlines())
    print(f'01 part 1: {total_score(lines)}')

def test_3():
    lines = list(open('02.txt').read().splitlines())
    print(f'01 part 2: {must_end_like(lines)}')
