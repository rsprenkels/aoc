# solution to https://adventofcode.com/2022/day/19
import copy
from collections import defaultdict, namedtuple
from typing import List
import re

aoc_day_number = '19'

QI = namedtuple("QI", "minutes ore clay obs geode ore_bot clay_bot obs_bot geode_bot")

class QI:
    def __init__(self, minutes, ore, clay, obs, geode, ore_b, clay_b, obs_b, geode_b):
        self.minutes = minutes
        self.ore = ore
        self.clay = clay
        self.obs = obs
        self.geode = geode
        self.ore_b = ore_b
        self.clay_b = clay_b
        self.obs_b = obs_b
        self.geode_b = geode_b

    def inc(self):
        self.minutes += 1
        self.ore += self.ore_b
        self.clay += self.clay_b
        self.obs += self.obs_b
        self.geode += self.geode_b

    def __repr__(self):
        return f'<{self.minutes} {self.ore} {self.ore_b}>'

    def __lt__(self, other):
        return self.minutes < other.minutes

def options(bp, qi):
    """
    :param bp: the blueprint
    :param qi: the current queue item
    :return: a generator for the options for this queue item
    """
    orig_qi = copy.deepcopy(qi)
    qi = copy.deepcopy(qi)
    qi.inc()
    yield qi
    for ore_b in range(1, (orig_qi.ore // int(bp['ore_ore'])) + 1):
        new_qi = copy.deepcopy(qi)
        new_qi.ore -= ore_b * int(bp['ore_ore'])
        new_qi.ore_b += ore_b
        yield new_qi
        # for opt in options(bp, new_qi):
        #     yield opt


def max_geodes(blueprint, max_minutes):
    queue = [QI(0, 0, 0, 0, 0, 1, 0, 0, 0)]
    cur_max_geodes = 0
    seen = set()
    while queue:
        qi = queue.pop(0)
        seen.add(qi)
        if qi.minutes == max_minutes:
            cur_max_geodes = max(cur_max_geodes, qi.geode)
        else:
            for new_qi in options(blueprint, qi):
                queue.append(new_qi)
                pass
    return len(list(seen))

def solution(lines: List[str], part=1):
    pattern = r"Blueprint (?P<blueprint>\d+): Each ore robot costs (?P<ore_ore>\d+) ore. Each clay robot costs (?P<clay_ore>\d+) ore. Each obsidian robot costs (?P<obs_ore>\d+) ore and (?P<obs_clay>\d+) clay. Each geode robot costs (?P<geode_ore>\d+) ore and (?P<geode_obs>\d+) obsidian."
    quality_level = 0
    for line in lines:
        blueprint = re.search(pattern, line).groupdict()
        quality_level += max_geodes(blueprint, max_minutes=11)
    return quality_level


demo_input = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".split('\n')

# def test_options(lines: List[str] = demo_input):
#     queue = [QI(0, 10, 0, 0, 0, 1, 0, 0, 0)]
#     pattern = r"Blueprint (?P<blueprint>\d+): Each ore robot costs (?P<ore_ore>\d+) ore. Each clay robot costs (?P<clay_ore>\d+) ore. Each obsidian robot costs (?P<obs_ore>\d+) ore and (?P<obs_clay>\d+) clay. Each geode robot costs (?P<geode_ore>\d+) ore and (?P<geode_obs>\d+) obsidian."
#     quality_level = 0
#     for line in lines[:1]:
#         bp = re.search(pattern, line).groupdict()
#         print('\n', list(options(bp, queue[0])))


def test_demo_input_part1():
    print()
    assert solution([l for l in demo_input]) == 33

# def test_part_1():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 1: {solution(lines)}', end='')
#
# def test_demo_input_part2():
#     assert solution([l for l in demo_input], part=2) == 58
#
# def test_part_2():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 2: {solution(lines, part=2)}', end='')
