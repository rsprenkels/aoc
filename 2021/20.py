a = open('20.txt').read().splitlines()
alg = a[0]
image = a[2:]
out = []
w,h = len(image[0]), len(image)
print(f'w:{w} h:{h}')
for loop in range(2):
    new_image = []
    for y, line in enumerate(image):
        nl = []
        for x, c in enumerate(line):
            code = []
            for dx, dy in ((dx,dy) for dy in range(-1,2) for dx in range(-1,2)):
                if x + dx in range(w) and y + dy in range(h):
                    code.append('1' if image[y+dy][x+dx] == '#' else '0')
                    print(f'x:{x} y:{y} ({dx},{dy}) p:{x+dx},{y+dy}', end=' ')
                    print()
                else:
                    code.append('0')
            nl.append(alg[int("".join(code),2)])
            print(f'({x},{y}) {alg[int("".join(code),2)]}')
        new_image.append(''.join(nl))
    print('\n'.join(new_image))
    image = new_image

res_part1 = sum(1 for p in line for line in new_image if p == '#')
print(f'part1: {res_part1}')
# 5700 too high