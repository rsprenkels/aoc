from collections import defaultdict
lines = open('8.txt').read().splitlines()

segs_on = [6,2,5,5,4,5,6,3,7,6]
num_segs_on = [b for a,b in list(zip(range(10), segs_on)) if a in [1,4,7,8]]

encodings = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
# sorted([(a,b) for a,b in list(zip(range(10), segs_on))], key=lambda x: x[1])
# [(1, 2), (7, 3), (4, 4), (2, 5), (3, 5), (5, 5), (0, 6), (6, 6), (9, 6), (8, 7)]
# 2: 1
# 3: 7
# 4: 4
# 5: 2,3,5
# 6: 0,6,9
# 7: 8
dig_count = 0
for line in lines:
    left, right = line.split(' | ')
    digits = right.split()
    dig_count += sum([len(digit) in num_segs_on for digit in digits])
print(f'part 1: {dig_count}')


total = 0
for line in lines:
    left, right = line.split(' | ')
    observations = left.split()
    observations = [''.join(sorted(x)) for x in observations]
    print(observations)
    ob = defaultdict(list)
    for obs in observations:
        ob[len(obs)].append(obs)
    mapping = [''] * 10
    for k in sorted(ob.keys()):
        print(f'{k}: {ob[k]}')
    mapping[1] = ob[2][0]
    mapping[4] = ob[4][0]
    mapping[7] = ob[3][0]
    mapping[8] = ob[7][0]
    mapping[3] = next(k for k in ob[5] if all(c in k for c in mapping[1]))
    bd = set(ob[4][0]) - set(ob[2][0])
    mapping[5] = next(ob5 for ob5 in ob[5] if bd.issubset(set(ob5)))
    mapping[2] = next(ob5 for ob5 in ob[5] if ob5 not in [mapping[5], mapping[3]])
    mapping[6] = next(ob6 for ob6 in ob[6] if not set(mapping[1]).issubset(set(ob6)))
    mapping[9] = next(ob6 for ob6 in ob[6] if set(mapping[4]).issubset(set(ob6)))
    mapping[0] = next(ob6 for ob6 in ob[6] if ob6 not in [mapping[6], mapping[9]])
    digits = [''.join(sorted(x)) for x in right.split()]
    print(f'digits: {digits}')
    number = int(''.join([str(mapping.index(d)) for d in digits]))
    print(f'number: {number}')
    total += number
    print(mapping)

print(f'part 2: {total}')