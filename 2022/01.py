# solution to https://adventofcode.com/2022/day/1

def max_calories(lines):
    elves = []
    current_elve = []
    for line in lines:
        if line != '':
            current_elve.append(int(line))
        else:
            elves.append(current_elve)
            current_elve = []
    elves.append((current_elve))
    one_elve =  max((sum(elve) for elve in elves))
    top_three_elves = sum(sorted((sum(elve) for elve in elves))[-3:])
    return (one_elve, top_three_elves)

def test_1():
    lines = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".split('\n')

    assert max_calories(lines)[0] == 24000
    assert max_calories(lines)[1] == 45000

def test_2():
    lines = list(open('01.txt').read().splitlines())
    print(f'01 part 1: {max_calories(lines)[0]}')

def test_3():
    lines = list(open('01.txt').read().splitlines())
    print(f'01 part 2: {max_calories(lines)[1]}')
