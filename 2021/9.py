from functools import reduce
grid = [list(map(int,(c for c in line))) for line in open('9.txt').read().splitlines()]
print(grid)
risk_level = 0
basins = []
for x in range(w := len(grid[0])):
    for y in range(h := len(grid)):
        is_lowpoint = True
        for tx, ty in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
            if tx >= 0 and tx < w and ty >= 0 and ty < h:
                print(f'w: {w} h: {h} x: {x} y: {y} tx: {tx} ty: {ty}')
                if grid[ty][tx] <= grid[y][x]:
                    is_lowpoint = False
        if is_lowpoint:
            basins.append((x,y))
            print(f'lowpoint: {x,y}')
            risk_level += grid[y][x] + 1
print(f'part 1: {risk_level}')

basin_sizes = []
for b in basins:
    size = 0
    to_visit = [b]
    seen = []
    while to_visit:
        x,y = to_visit.pop(0)
        seen.append((x,y))
        size += 1
        for tx, ty in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
            if tx >= 0 and tx < w and ty >= 0 and ty < h:
                if (v := grid[ty][tx]) >= grid[y][x] and v != 9 and (tx,ty) not in seen and (tx,ty) not in to_visit:
                    to_visit.append((tx, ty))
    basin_sizes.append(size)
    print(f'basin: {seen[0]} size: {size}')
basin_sizes.sort(reverse=True)
print(f'part 2: {(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])}')

# 53805081981 is too high
# 289079232 still too high