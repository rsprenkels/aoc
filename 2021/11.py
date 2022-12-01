a = [list(map(int, [c for c in line])) for line in open('11.txt').read().splitlines()]

def show():
    for y in range(10):
        for x in range(10):
            print(a[y][x], sep='', end='')
        print()
    print()

flashes = 0
for gen in range(100):
    for y in range(10):
        for x in range(10):
            a[y][x] += 1
    needs_flash = []
    has_flashed = []
    for y in range(10):
        for x in range(10):
            if a[y][x] > 9:
                needs_flash.append((x,y))
    while needs_flash:
        x,y = needs_flash.pop(0)
        has_flashed.append((x,y))
        for dx,dy in [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]:
            if (nx := x+dx) >= 0 and nx < 10 and (ny := y+dy) >= 0 and ny < 10:
                a[ny][nx] += 1
                if a[ny][nx] > 9 and (nx,ny) not in has_flashed and (nx,ny) not in needs_flash:
                    needs_flash.append((nx,ny))
    for x,y in has_flashed:
        flashes += 1
        a[y][x] = 0

print(f'part1: {flashes}')

a = [list(map(int, [c for c in line])) for line in open('11.txt').read().splitlines()]
gen = 0
all_flashed = False
while not all_flashed:
    gen += 1
    for y in range(10):
        for x in range(10):
            a[y][x] += 1
    needs_flash = []
    has_flashed = []
    for y in range(10):
        for x in range(10):
            if a[y][x] > 9:
                needs_flash.append((x,y))
    while needs_flash:
        x,y = needs_flash.pop(0)
        has_flashed.append((x,y))
        for dx,dy in [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]:
            if (nx := x+dx) >= 0 and nx < 10 and (ny := y+dy) >= 0 and ny < 10:
                a[ny][nx] += 1
                if a[ny][nx] > 9 and (nx,ny) not in has_flashed and (nx,ny) not in needs_flash:
                    needs_flash.append((nx,ny))
    flashes = 0
    for x,y in has_flashed:
        flashes += 1
        a[y][x] = 0
    all_flashed = flashes == 100

print(f'part2: {gen}')

#1389 is too low
#1689 is too high
#1656 also too high


