readings = list(int(line) for line in open('1.txt').readlines())

print('part 1: ', end='')
print(len([1 for n in range(len(readings)-1) if readings[n+1] > readings[n]]))

print('part 2: ', end='')
print(len([1 for n in range(len(readings)-2) if sum(readings[n+1:n+4]) > sum(readings[n:n+3])]))
