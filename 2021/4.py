from typing import List

lines = list(open('4.txt').read().splitlines())
numbers = list(map(int, lines.pop(0).split(',')))

class Board:
    def __init__(self, lines: List[str]):
        self.rows = [list(map(int, line.split())) for line in lines]
        self.seen = [[False for _ in range(5)] for _ in range(5)]

    def __repr__(self) -> str:
        return '\n' + '\n'.join([' '.join(f'{d:>2}' for d in list(map(str, row))) for row in self.rows]) + '\n'

    def mark(self, n:int) -> bool:
        for rndx, row in enumerate(self.rows):
            for cndx in range(len(row)):
                if row[cndx] == n:
                    self.seen[rndx][cndx] = True
                    if all(self.seen[rndx]) or all([self.seen[r][cndx] for r in range(5)]):
                        return True
        return False

    def sum_unmarked(self) -> int:
        return sum(self.rows[r][c] for c in range(5) for r in range(5) if not self.seen[r][c])

boards = []

while lines:
    board = []
    lines.pop(0)
    boards.append(Board(lines[:5]))
    lines = lines[5:]

# drawn = []
# game_running = True
# while game_running:
#     drawn.append(n := numbers.pop(0))
#     for b in boards:
#         if b.mark(n):
#             # print(f'drawn: {" ".join(map(str, drawn))}')
#             # print(b)
#             print(f'part 1: {b.sum_unmarked() * n}')
#             game_running = False

won_value = None

for n in numbers:
    new_boards = []
    for b in boards:
        if b.mark(n):
            won_value = b.sum_unmarked() * n
            print(f'won board {b, n, won_value}')
        else:
            new_boards.append(b)
    boards = new_boards

print(f'part 2: {won_value}')

# 43974 is too low
# part 1: 64084