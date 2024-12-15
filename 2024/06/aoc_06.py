def solution(lines):
    return 41,42

def test_01():
    lines = """
""".split('\n')[1:-1]
    outcome = solution(lines)
    assert outcome[0] == 41
    # assert outcome[1] == 123


if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day {(day_no := 5)} part 1:{solution(lines)}')
