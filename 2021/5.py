lines = list(open('5_orig.txt').read().splitlines())
lines_endpoints = []
for line in lines:
    p_from, p_to = line.split(' -> ')
    lines_endpoints.append([tuple(map(int, p_from.split(','))), tuple(map(int, p_to.split(',')))])

points = [[0 for _ in range(1000)] for _ in range(1000)]
for line in lines_endpoints:
    a, b = line
    if a[0] == b[0]: # x are equal
        for y in range(min(a[1], b[1]), max(a[1], b[1])+1):
            points[a[0]][y] += 1
    elif a[1] == b[1]: # y are equal
        for x in range(min(a[0],b[0]), max(a[0],b[0])+1):
            points[x][a[1]] += 1

res_1 = sum(p>1 for row in points for p in row)
print(f'part 1: {res_1}')

for line in lines_endpoints:
    a, b = line
    if a[0] != b[0] and a[1] != b[1]:
        x,y = a[0],a[1]
        xdir = 1 if b[0] > a[0] else -1
        ydir = 1 if b[1] > a[1] else -1
        for _ in range(abs(b[0]-a[0])+1):
            print(f'a:{a} b:{b} x:{x},y:{y}')
            points[x][y] += 1
            x += xdir
            y += ydir
            if (a,b) == ((580,153),(274,459)):
                print(x,y)

res_2 = sum(p>1 for row in points for p in row)
print(f'part 2: {res_2}')

# 22952 still too high
# 23026 cannot be right then either
# 20352 is just wrong
# 20373 is ,,,,,
# 9721 too low