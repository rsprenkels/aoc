from typing import List
import re

def solution(lines: List[str]) -> int:
    return sum([int(digit_list[0] + digit_list[-1]) for digit_list in [[d for d in line if d.isdigit()] for line in lines]])

def test_01():
    lines = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split('\n')
    assert solution(lines) == 142


def sol_part2(lines):
    map = {k:str(v) for v,k in enumerate('one two three four five six seven eight nine'.split(), start=1)}
    rev_map = {k:str(v) for v,k in enumerate('eno owt eerht ruof evif xis neves thgie enin'.split(), start=1)}
    def replace_with_number(match_obj):
        m = match_obj.group(0)
        # return map[m]
        return map[m]
    def replace_with_number_rev(match_obj):
        m = match_obj.group(0)
        # return map[m]
        return rev_map[m]
    total = 0
    expression = 'one|two|three|four|five|six|seven|eight|nine'
    exp_forward = f'({expression})'
    exp_reversed = f'({expression[::-1]})'
    for line in lines:
        res_forward = re.sub(exp_forward, replace_with_number, line)
        dig_first = [d for d in res_forward if d.isdigit()][0]
        res_reversed = re.sub(exp_reversed, replace_with_number_rev, line[::-1])
        dig_last = [d for d in res_reversed if d.isdigit()][0]
        number = int(dig_first + dig_last)
        print(f'{line} {number}')
        total += number
    print(f'I got {len(lines)} lines')
    return total

def test_02():
    lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split('\n')
    assert sol_part2(lines) == 281

def test_03():
    lines = """pcg91vqrfpxxzzzoneightzt""".split('\n')
    assert sol_part2(lines) == 98



if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day 01 part 1:{solution(lines)}')
    print(f'day 01 part 2:{sol_part2(lines)}')


