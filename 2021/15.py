import math

map = [[int(c) for c in line] for line in open('15.txt').read().splitlines()]
bottom_right = ((width := len(map[0])), (height := len(map)))
print(f'bottom_right: {bottom_right}')
cost = [[math.inf for _ in range(width)] for _ in range(height)]
cost[0][0] = 0
Q = [(0, 0)]
while Q:
    print(f'{len(Q):6} {cost[-1][-1]}')
    cur_loc = Q.pop()
    x, y = cur_loc
    for dx, dy in [(1,0), (0,1)]:
        if (nx := x+dx) >= 0 and nx < width and (ny := y+dy) >= 0 and ny < height:
            if (new_cost := cost[y][x] + map[ny][nx]) < cost[ny][nx] and (cost[-1][-1] == math.inf or new_cost < cost[-1][-1]):
                cost[ny][nx] = new_cost
                Q.append((nx,ny))

print(f'part1: {cost[-1][-1]}')

nmap = []
for line in map:
    nmap.append([(r + h - 1)%9 + 1 for h in range(5) for r in line])
for v in range(1,5):
    for line in nmap[:height]:
        nmap.append([(r + v - 1)%9 + 1 for r in line])

for line in nmap:
    print(''.join([str(c) for c in line]))

bottom_right = ((width := len(nmap[0])), (height := len(nmap)))
cost = [[math.inf for _ in range(width)] for _ in range(height)]
cost[0][0] = 0
Q = [(0,0)]
count = 0


def manhattan_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

min_x, max_x, min_y, max_y = 1000,0,1000,0

while Q:
    count += 1
    if count % 1000000 == 0:
        print(f'{count // 1000000:10} {len(Q):6} {cost[-1][-1]} x:{min_x}-{max_x}  y:{min_y}-{max_y}')
    cur_loc = Q.pop()
    x,y = cur_loc
    for dx, dy in [(0,1),(1,0),]:
        if (nx := x+dx) >= 0 and nx < width and (ny := y+dy) >= 0 and ny < height:
            min_x = min(nx, min_x)
            max_x = max(nx, max_x)
            min_y = min(ny, min_y)
            max_y = max(ny, max_y)
            if (new_cost := cost[y][x] + nmap[ny][nx]) < cost[ny][nx]:
                cost[ny][nx] = new_cost
                if (new_cost + manhattan_dist((nx,ny),(width,height)) < 2968):
                    Q.append((nx,ny))

print(f'part2: {cost[-1][-1]}')
# 2970 too high
# 2969 too high
# 2968 too high
# 2900 is just wrong
# 2963 is CORRECT!