from collections import defaultdict

map = list(open('12.txt').read().splitlines())
tree = defaultdict(set)
for line in map:
    a,b = line.split('-')
    tree[a].add(b)
    tree[b].add(a)

Q = [('start', [])]
seen = set()
found_paths = []

while Q:
    next_node, path = Q.pop()
    for node in tree[next_node]:
        if node == 'end':
            found_paths.append(path + [next_node, node])
        elif node != 'start' and not (len(node) <= 2 and node.islower() and node in path):
            Q.append((node, path + [next_node]))

print(f'part1: {len(found_paths)}')

Q = [('start', [])]
seen = set()
found_paths = []


def is_allowed(node, path):
    p = [n for n in path + [node] if n.islower() and len(n)<= 2]
    totals = [sum([n == u for n in p]) for u in set(p)]
    res =  sum([t == 2 for t in totals]) <= 1 and sum([t > 2 for t in totals]) == 0
    return res
    # return not (len(node) <= 2 and node.islower() and node in path)


while Q:
    next_node, path = Q.pop()
    for node in tree[next_node]:
        if node == 'end':
            found_paths.append(path + [next_node, node])
        elif node != 'start' and is_allowed(node, path + [next_node]):
            Q.append((node, path + [next_node]))

print(f'part2: {len(found_paths)}')


