lines = open('13.txt').read().splitlines()
points = set()
while lines[0] != '':
    x,y = map(int,lines.pop(0).split(','))
    points.add((x,y))
lines.pop(0)
folds = []
while lines:
    x_or_y, foldline = lines.pop(0)[11:].split('=')
    folds.append((x_or_y, int(foldline)))

ndx = 0
for x_or_y, foldline in folds:
    ndx += 1
    npoints = set()
    if x_or_y == 'x':
        for x,y in points:
            if x < foldline:
                npoints.add((x,y))
            else:
                npoints.add((2 * foldline - x, y))
    else:
        for x,y in points:
            if y < foldline:
                npoints.add((x,y))
            else:
                npoints.add((x, 2 * foldline - y))
    points = npoints
    if ndx == 1:
        print(f'part1: {len(points)}')

for y in range(7):
    for x in range(55):
        print('#' if (x,y) in points else ' ', sep='', end='')
    print()