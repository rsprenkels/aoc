from itertools import permutations
from typing import List

sf_number_lines = open('18.txt').read().splitlines()

def parse_sf_number(tokens: List[str]):
    # print(f'parsing {tokens}')
    if tokens[0] == '[': # it is a pair
        tokens.pop(0) # consume the token
        first = parse_sf_number(tokens)
        if tokens.pop(0) != ',': exit(2)
        second = parse_sf_number(tokens)
        if tokens.pop(0) != ']': exit(3)
        return [first, second]
    else: # its a single element
        element = int(tokens.pop(0))
        return element

sf_numbers = [parse_sf_number(list(line)) for line in sf_number_lines]

def sf_reduce(sfn):
    print(f'reducing {sfn}')
    sfn = f'{sfn}'.replace(' ','')
    action_executed = True
    while action_executed:
        action_executed = False
        # print(f'{type(sfn)}   {sfn}')
        level = 0
        new_sfn = None
        for ndx, c in enumerate(sfn):
            if c == '[':
                level += 1
            elif c == ']':
                level -= 1
            if level == 5 and c == '[':
                left_part = sfn[:ndx]
                l_num = ''; ndx += 1
                while sfn[++ndx].isdigit():
                    l_num += sfn[ndx]
                    ndx += 1
                r_num = ''
                ndx += 1
                while sfn[++ndx].isdigit():
                    r_num += sfn[ndx]
                    ndx += 1
                right_part = sfn[ndx:]
                print(f'{sfn} l_num:{l_num} r_num:{r_num} left:{left_part} right:{right_part}')
                for r_ndx, c in enumerate(right_part):
                    if c.isdigit():
                        v = ''
                        pndx = r_ndx
                        while right_part[pndx].isdigit():
                            v += right_part[pndx]
                            pndx += 1
                        nv = str(int(r_num) + int(v))
                        right_part = right_part[1:r_ndx] + nv + right_part[pndx:]
                        break
                print(f'new_right_part:{right_part}')
                for l_ndx, c in reversed(list(enumerate(left_part))):
                    # print(f'l_ndx:{l_ndx} p:{p}')
                    if c.isdigit():
                        v = ''
                        pndx = l_ndx
                        while left_part[pndx].isdigit():
                            v = left_part[pndx] + v
                            pndx -= 1
                        nv = str(int(l_num) + int(v))
                        left_part = left_part[:pndx+1] + nv + left_part[l_ndx+1:]
                        print(f'new left_part:{left_part}')
                        break
                sfn = left_part + '0' + right_part
                print(f'result: {sfn}')
                action_executed = True
                break
        if not action_executed:
            for s_ndx, p in enumerate(zip(sfn, sfn[1:])):
                c1, c2 = p
                if c1.isdigit() and c2.isdigit():
                    print(f'{sfn} need to split {"".join(p)}')
                    action_executed = True
                    bv = int("".join(p))
                    sfn = sfn[:s_ndx] + f'[{bv // 2},{bv - bv // 2}]' + sfn[s_ndx+2:]
                    break
    print(f'final result: {sfn}')
    return parse_sf_number(list(sfn))

while len(sf_numbers) > 1:
    sf_numbers[0] = sf_reduce([sf_numbers[0],sf_numbers[1]])
    print()
    print()
    sf_numbers.pop(1)


def magnitude(sfn):
    tokens = list(f'{sfn}'.replace(' ',''))

    def calc_magnitude(tokens):
        if tokens[0] == '[': # it is a pair
            tokens.pop(0) # consume the token
            first = calc_magnitude(tokens)
            if tokens.pop(0) != ',': exit(2)
            second = calc_magnitude(tokens)
            if tokens.pop(0) != ']': exit(3)
            return 3 * first + 2 * second
        else: # its a single element
            element = int(tokens.pop(0))
            return element

    return calc_magnitude(tokens)


print(f'part1: {magnitude(sf_numbers[0])}')

sf_numbers = [parse_sf_number(list(line)) for line in sf_number_lines]

max_mag = 0
for a, b in list(permutations(sf_numbers, 2)):
    mag = magnitude(sf_reduce([a,b]))
    max_mag = max(max_mag, mag)

print(f'part2: {max_mag}')
# [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]

# result = sf_reduce([sf_numbers[0],sf_numbers[1]])
# print(f'result:{result} n1:{sf_numbers[0]} n2:{sf_numbers[1]}')

# sfn = parse_sf_number(list('[[[[[9,8],1],2],3],4]'))
# sfn = parse_sf_number(list('[7,[6,[5,[4,[3,2]]]]]'))
# sfn = parse_sf_number(list('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'))
# sfn = parse_sf_number(list('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'))
# print(f'reducing {sfn} gives {sf_reduce(sfn)}')