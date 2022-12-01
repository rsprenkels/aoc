from collections import defaultdict
from typing import Tuple

lines = open('10.txt').read().splitlines()

def analyse(line: str) -> Tuple[str, str]:
    chars = list(line)
    stack = []
    char_pairs = {'(':')', '[':']', '{':'}', '<':'>'}
    while chars:
        c = chars.pop(0)
        # print(f'c:{c} stack:{stack}')
        if c in char_pairs.keys():
            stack.append(c)
        elif c in char_pairs.values():
            if len(stack)>0 and c in char_pairs.values() and char_pairs[stack[-1]] == c:
                stack.pop()
            else:
                return ('corrupted', c)
    if stack:
        return ('incomplete', stack)
    else:
        return ('ok', '')

char_count = defaultdict(int)

part2_score = []

for line in lines:
    # print(f'line: {line}')
    result, param = analyse(line)
    if result == 'corrupted':
        char_count[param] += 1
    elif result == 'incomplete':
        score = 0
        for c in param[::-1]:
            score = score * 5 + {'(':1, '[':2, '{':3, '<':4}[c]
        part2_score.append(score)
    # print()

char_values = {')':3, ']':57, '}':1197, '>':25137}

print(f'part 1: {sum([char_values[c] * char_count[c] for c in char_values.keys()])}')
print(f'part 2: {sorted(part2_score)[len(part2_score) // 2]}')

# 759156 too high.

# part2 263458535094 too high
#       27991386033 also