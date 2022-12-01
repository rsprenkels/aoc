c = list(map(int, open('7.txt').readline().split(',')))
print(min([(t, sum(abs(x-t) for x in c)) for t in range(min(c), max(c)+1)], key=lambda v: v[1]))
print(min([(t, sum(sum(range(abs(x-t)+1)) for x in c)) for t in range(min(c), max(c)+1)], key=lambda v: v[1]))