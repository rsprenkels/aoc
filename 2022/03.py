# solution to https://adventofcode.com/2022/day/3
import string

prios = string.ascii_lowercase + string.ascii_uppercase

def sum_priorities(lines):
    total_prio = 0
    for rucksack in lines:
        first, second = (rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:])
        in_both = [item for item in first if item in second][0]
        total_prio += prios.index(in_both) + 1
    return total_prio

def sum_groups_of_three(lines):
    total_prio = 0
    for elv_ndx in range(0, len(lines), 3):
        for item in lines[elv_ndx]:
            if item in lines[elv_ndx+1] and item in lines[elv_ndx+2]:
                total_prio += prios.index(item) + 1
                break
    return total_prio

def test_demo_input():
    lines = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split('\n')
    assert sum_priorities(lines) == 157
    assert sum_groups_of_three(lines) == 70

def test_2():
    lines = list(open('03.txt').read().splitlines())
    print(f'03 part 1: {sum_priorities(lines)}')

def test_3():
    lines = list(open('03.txt').read().splitlines())
    print(f'03 part 2: {sum_groups_of_three(lines)}')
