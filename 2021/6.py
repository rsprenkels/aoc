f = list(map(int, open('6.txt').readline().split(',')))
f_orig = f[:]
for day in range(80):
    extra_fish = 0
    for ndx, d in enumerate(f):
        if d == 0:
            f[ndx] = 6
            extra_fish += 1
        else:
            f[ndx] -= 1
    for _ in range(extra_fish):
        f.append(8)

print(f'part 1: {len(f)}')

dsum = [0] * 9
for fish in f_orig:
    dsum[fish] += 1
for day in range(256):
    new_dsum = [0] * 9
    for n in range(8):
        new_dsum[n] = dsum[n+1]
    new_dsum[6] += dsum[0]
    new_dsum[8] = dsum[0]
    dsum = new_dsum
print(f'part 2: {sum(dsum)}')
