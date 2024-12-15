from typing import List
import re


def inrange(end, maxval):
    return end >= 0 and end < maxval

def solution(lines: List[str]) -> int:
    word = 'XMAS'
    matches = 0
    g = [[c for c in line] for line in lines]
    w, h = len(lines[0]), len(lines)
    for y in range(h):
        for x in range(w):
            if g[y][x] == word[0]:
                for direction in [(-1,0), (-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]:
                    dx,dy = direction
                    if inrange(x + 3*dx, w) and inrange(y + 3*dy, h):
                        if all(g[y+dy*c][x+dx*c] == word[c] for c in range(1, len(word))):
                            matches += 1
    return matches

def solution_p2(lines: List[str]) -> int:
    word = 'MAS'
    matches = 0
    g = [[c for c in line] for line in lines]
    w, h = len(lines[0]), len(lines)
    for y in range(h):
        for x in range(w):
            if g[y][x] == word[1]:
                for direction in [(1,1)]:
                    if x>0 and x<w-1 and y>0 and y<h-1:
                        dx,dy = direction
                        w1 = g[y+dy][x+dx] + word[1] + g[y-dy][x-dx]
                        w2 = g[y-dx][x+dy] + word[1] + g[y+dx][x-dy]
                        if w1 in [word, word[::-1]] and w2 in [word, word[::-1]]:
                            matches += 1
    return matches


def test_01():
    test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".split('\n')[1:-1]
    assert solution(test_input) == 18
    assert solution_p2(test_input) == 9


if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day 04 part 1:{solution(lines)}')
    print(f'day 04 part 2:{solution_p2(lines)}')
