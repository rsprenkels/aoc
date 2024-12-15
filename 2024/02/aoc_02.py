from typing import List


def safe(n):
    all_diff = all(a != b for a,b in zip(n, n[1:]))
    same_direction = all([a > b for a, b in zip(n, n[1:])]) or all([a < b for a, b in zip(n, n[1:])])
    small_steps = all([abs(a-b) <= 3 for a, b in zip(n, n[1:])])
    return all_diff and same_direction and small_steps

def list_minus_element(l: List, n: int) -> List:
    copy_l = l.copy()
    copy_l.pop(n)
    return copy_l

def safe2(n):
    return any(safe(k) for k in [list_minus_element(n, p) for p in range(len(n))])

def solution(lines: List[str]):
    return sum(1 for n in [list(map(int, line.split())) for line in lines] if safe(n))

def solution_part2(lines: List[str]):
    return sum(1 for n in [list(map(int, line.split())) for line in lines] if safe2(n))


def test_01():
    test_input = """"
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9 
""".split('\n')[1:-1]
    assert solution(test_input) == 2


def test_02():
    test_input = """"
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9 
""".split('\n')[1:-1]
    assert solution_part2(test_input) == 4

if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day 02 part 1:{solution(lines)}')
    print(f'day 02 part 1:{solution_part2(lines)}')
