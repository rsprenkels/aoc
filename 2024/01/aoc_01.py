def solution(lines):
    left = []
    right = []
    for line in lines:
        a, b = map(int, line.split('   '))
        left.append(a)
        right.append(b)
    return sum((abs(a - b) for a, b in zip(sorted(left), sorted(right))))


def solution_part2(lines):
    left = []
    right = []
    for line in lines:
        a, b = map(int, line.split('   '))
        left.append(a)
        right.append(b)
    return sum(list(len(list(b for b in right if b == a)) * a for a in left))


def test_01():
    lines = """
3   4
4   3
2   5
1   3
3   9
3   3
""".split('\n')
    assert solution(lines[1:-1]) == 11



def test_02():
    lines = """
3   4
4   3
2   5
1   3
3   9
3   3
""".split('\n')
    assert solution_part2(lines[1:-1]) ==31


if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day 01 part 1:{solution(lines)}')
    print(f'day 01 part 2:{solution_part2(lines)}')
