def order_is_valid(order, rules):
    for a,b in rules:
        if a in order and b in order and order.index(a) > order.index(b):
            return False
    return True

def re_order(order, rules):
    print(f'starting order is {order}')
    swaps_done = True
    while swaps_done:
        swaps_done = False
        for a,b in rules:
            if a in order and b in order and (idx_a := order.index(a)) > (idx_b := order.index(b)):
                order[idx_a], order[idx_b] = order[idx_b], order[idx_a]
                print(f'rule {a},{b} gives {order}')
                swaps_done = True
    return order

def solution(lines):
    rules = []
    while lines[0] != '':
        line = lines.pop(0)
        a,b = list(map(int, line.split('|')))
        rules.append((a,b))
    lines.pop(0)
    orders = []
    while lines:
        line = lines.pop(0)
        orders.append(list(map(int, line.split(','))))

    total_sum = 0
    corrected_sum = 0
    for order in orders:
        if order_is_valid(order, rules):
            total_sum += order[len(order) // 2]
        else:
            order = re_order(order, rules)
            corrected_sum += order[len(order) // 2]
    return total_sum, corrected_sum

def solution_p2(lines):
    pass


def test_01():
    lines = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".split('\n')[1:-1]
    outcome = solution(lines)
    assert outcome[0] == 143
    assert outcome[1] == 123


if __name__ == '__main__':
    lines = list(open('input.txt').read().splitlines())
    print(f'day {(day_no := 4)} part 1:{solution(lines)}')
    print(f'day {day_no} part 2:{solution_p2(lines)}')