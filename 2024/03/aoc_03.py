from typing import List
import re

def solution(lines: List[str]) -> int:
    total = 0
    for line in lines:
        matches = re.finditer(r'mul\((\d+),(\d+)\)', line)
        for match in matches:
            total += int(match.group(1)) * int(match.group(2))
    return total

def solution_p2(lines: List[str]) -> int:
    total = 0
    enabled = True
    for line in lines:
        matches = re.finditer(r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)', line)
        for match in matches:
            if match.group(0) == 'do()':
                enabled = True
            elif match.group(0) == 'don\'t()':
                enabled = False
            else:
                if enabled:
                    total += int(match.group(1)) * int(match.group(2))
    return total


def test_01():
    test_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".split('\n')[1:-1]
    assert solution(test_input) == 161


def test_02():
    test_input = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".split('\n')[1:-1]
    assert solution_p2(test_input) == 48


if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day 03 part 1:{solution(lines)}')
    print(f'day 03 part 2:{solution_p2(lines)}')
