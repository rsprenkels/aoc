# solution to https://adventofcode.com/2022/day/5

aoc_day_number = '08'


def solution(lines):
    trees = [[int(tree) for tree in line ]for line in lines]
    visible_inner_trees = []
    width, height = len(trees[0]), len(trees)
    for y in range(1, height-1):
        for x in range(1, width-1):
            v_up =    all(trees[a][x] < trees[y][x] for a in range(y-1, -1, -1))
            v_down =  all(trees[a][x] < trees[y][x] for a in range(y+1, height))
            v_left =  all(trees[y][a] < trees[y][x] for a in range(x-1, -1, -1))
            v_right = all(trees[y][a] < trees[y][x] for a in range(x+1, width))
            if v_up or v_down or v_left or v_right:
                visible_inner_trees.append((x,y))
    return 2 * width + 2 * height - 4 + len(visible_inner_trees)


def solution_part2(lines):
    trees = [[int(tree) for tree in line ]for line in lines]
    scenic_score = (0, (0,0))
    width, height = len(trees[0]), len(trees)
    for y in range(1, height-1):
        for x in range(1, width-1):
            v_up = 0
            for a in range(y-1, -1, -1):
                v_up += 1
                if trees[a][x] >= trees[y][x]:
                    break
            v_down = 0
            for a in range(y+1, height):
                v_down += 1
                if trees[a][x] >= trees[y][x]:
                    break
            v_left = 0
            for a in range(x-1, -1, -1):
                v_left += 1
                if trees[y][a] >= trees[y][x]:
                    break
            v_right = 0
            for a in range(x+1, width):
                v_right += 1
                if trees[y][a] >= trees[y][x]:
                    break
            if (cur_ss := v_up * v_down * v_left * v_right) > scenic_score[0]:
                scenic_score = (cur_ss, (x,y))
    return  scenic_score[0]


def test_demo_input():
    lines = """30373
25512
65332
33549
35390""".split('\n')
    assert solution([l for l in lines]) == 21


def test_demo_input_part2():
    lines = """30373
25512
65332
33549
35390""".split('\n')
    assert solution_part2([l for l in lines]) == 8


def test_part_1():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')


def test_part_2():
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f' day {aoc_day_number} part 2: {solution_part2(lines)}', end='')

