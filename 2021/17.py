import math

target_spec = open('17.txt').readline().split()[2:]
x_range = tuple(map(int, target_spec[0][2:-1].split('..')))
y_range = tuple(map(int, target_spec[1][2:].split('..')))
print(x_range, y_range)

max_height = -math.inf


def simulate(vx, vy, x_range, y_range):
    x,y = 0,0
    max_height = y
    hit_target = False
    while not hit_target and (x <= max(x_range) and y >= min(y_range)):
        # print(f'vx:{vx} vy:{vy} x:{x} y:{y} ')
        x += vx
        y += vy
        max_height = max(max_height, y)
        if vx > 0: vx -= 1
        elif vx < 0: vx += 1
        vy -= 1
        hit_target = x >= x_range[0] and x <= x_range[1] and y >= y_range[0] and y <= y_range[1]
    return hit_target, max_height

tries = 0
hits = 0
for vx in range(max(x_range)*2):
    for vy in range(min(y_range)*4, abs(max(y_range))*4):
        if tries % 100000 == 0:
            print(f'tries: {tries // 100000:5}', end='')
            print(f'vx:{vx} vy:{vy} x_range:{x_range} y_range:{y_range}')
        is_hit, reached_height = simulate(vx, vy, x_range, y_range)
        if is_hit:
            hits += 1
            max_height = max(reached_height, max_height)
        tries += 1
print(f'part1: tries:{tries}  {max_height}')
print(f'part2: hits:{hits}')

#2: 3716 is too low.
