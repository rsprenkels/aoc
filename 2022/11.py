# solution to https://adventofcode.com/2022/day/11

aoc_day_number = '11'


def calc_wl(worry_level, operator, value):
    if operator == '*':
        if value == 'old':
            return worry_level ** 2
        else:
            return worry_level * int(value)
    elif operator == '+':
        return worry_level + int(value)
    else:
        raise Exception(f"unsupported operator {operator}")


def solution(lines, rounds=20, div_by=3):
    monkeys = []
    overall_div = 1
    while len(lines) >= 6:
        monkey = {}
        monkey['items'] = list(map(int, lines[1][len('  Starting items: '):].split(', ')))
        monkey['operator'], monkey['value'] = lines[2][len('  Operation: new = old '):].split(' ')
        monkey['div_by'] = int(lines[3][len('  Test: divisible by '):])
        overall_div *= monkey['div_by']
        monkey['if_true'] = int(lines[4][len('    If true: throw to monkey '):])
        monkey['if_false'] = int(lines[5][len('    If false: throw to monkey '):])
        monkey['inspect_count'] = 0
        monkeys.append(monkey)
        lines = lines[7:]
    for round in range(rounds):
        # if round % 100 == 0:
        #     print(f'round {round}')
        for ndx, m in enumerate(monkeys):
            for worry_level in m['items']:
                m['inspect_count'] += 1
                new_worry_level = calc_wl(worry_level, operator=m['operator'], value=m['value'])
                new_worry_level = new_worry_level // div_by
                new_worry_level %= overall_div
                if new_worry_level % m['div_by'] == 0:
                    target_monkey = m['if_true']
                else:
                    target_monkey = m['if_false']
                monkeys[target_monkey]['items'].append(new_worry_level)
            m['items'].clear()
        # for ndx, m in enumerate(monkeys):
        #     print(f'Monkey {ndx}: inspect: {m["inspect_count"]} {m["items"]}')
    monkeys = sorted(monkeys, key=lambda x: x['inspect_count'], reverse=True)
    return monkeys[0]['inspect_count'] * monkeys[1]['inspect_count']


def test_demo_input():
    lines = list(open(f'{aoc_day_number}_demo.txt').read().splitlines())
    assert solution([line for line in lines]) == 10605


def test_demo_input_part2():
    lines = list(open(f'{aoc_day_number}_demo.txt').read().splitlines())
    assert solution([line for line in lines], rounds=10000, div_by=1) == 2713310158


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')

def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution(lines, rounds=10000, div_by=1)}', end='')
