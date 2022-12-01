from collections import defaultdict
file = open('14.txt')
template = file.readline().strip()
orig_template = template
file.readline()
rule_lines = file.read().splitlines()
rules = {}
for rule in rule_lines:
    pair, add = rule.split(' -> ')
    rules[pair] = add
# print(rules)

#  CVKKFSSNNHNPSPPKBHPB

pair_count = defaultdict(int)

for pair in zip(template[:-1], template[1:]):
    pair_count[''.join(pair)] += 1

print(pair_count)

# for step in range(10):
#     new_template = ''
#     for ndx in range(len(template)-1):
#         if (key := template[ndx:ndx+2]) in rules.keys():
#             new_template += key[0] + rules[key]
#         else:
#             new_template += key[0]
#     new_template += template[-1:]
#     template = new_template
#     # print(f'step: {step+1} {template}')

for step in range(40):
    new_pairs = defaultdict(int)
    for p in pair_count.keys():
        if p in rules.keys():
            num_p = pair_count[p]
            new_pairs[p[0]+rules[p]] += num_p
            new_pairs[rules[p]+p[1]] += num_p
        else:
            new_pairs[p] += num_p
    pair_count = new_pairs
    print(f'step: {step} pairs: {pair_count}')

element_count = defaultdict(int)
for p in pair_count.keys():
    element_count[p[0]] += pair_count[p] / 2
    element_count[p[1]] += pair_count[p] / 2
element_count[orig_template[0]] += 0.5
element_count[orig_template[-1]] += 0.5

element_count = list(map(int, element_count.values()))
print(f'part1: 2375')
print(element_count)
print(f'part2: {max(element_count) - min(element_count)}')

