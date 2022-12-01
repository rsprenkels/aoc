lines = list(open('3.txt').read().splitlines())
# lines = ['10000000001', '10000000001', '01100000001', '01000000001']
print('\n'.join(lines))
num_cols = len(lines[0])
transposed = list([line[c:c+1] for line in lines] for c in range(len(lines[0])))
gamma = ''.join(['0' if sum([b=='0' for b in col]) > len(lines)//2 else '1' for col in transposed])
epsilon = ''.join(['0' if sum([b=='0' for b in col]) <= len(lines)//2 else '1' for col in transposed])

print(f'part one: {int(gamma,2) * int(epsilon,2)}')

ox = lines
co2 = [l for l in ox]

for cur_pos in range(len(lines[0])):
    transposed = list([line[c] for line in ox] for c in range(len(ox[0])))
    gamma = ''.join(['1' if sum([b=='1' for b in col]) >= len(ox)//2 else '0' for col in transposed])
    print(f'zeroes: {gamma} cur_pos: {cur_pos} len(ox): {len(ox)}')
    if(len(ox) <= 6):
        print('\n'.join(ox))
    ox = [line for line in ox if line[cur_pos] == gamma[cur_pos]]
    if len(ox) <= 1:
        print(f'ox: {ox}')
        ox=ox[0]
        break

for cur_pos in range(len(lines[0])):
    transposed = list([line[c] for line in co2] for c in range(len(co2[0])))
    gamma = ''.join(['0' if sum([b=='0' for b in col]) <= len(co2)//2 else '1' for col in transposed])
    print(f'ones: {gamma} cur_pos: {cur_pos} len(c02): {len(co2)}')
    if(len(co2) <= 6):
        print('\n'.join(co2))
    co2 = [line for line in co2 if line[cur_pos] == gamma[cur_pos]]
    if len(co2) <= 1:
        print(f'co2: {co2}')
        co2=co2[0]
        break

print(f'ox: {ox} co2: {co2}')

print(f'part two: {int(ox,2) * int(co2,2)}')
## 3958008 is too low

print(lines[:4])