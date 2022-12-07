# solution to https://adventofcode.com/2022/day/7
import logging
from collections import defaultdict
from typing import Tuple, List

aoc_day_number = '07'


class Directory:
    def __init__(self, full_path: str, parent: str = None):
        self.full_path = full_path
        self.children = []
        self.parent = parent
        self.total_size = 0


    def __repr__(self):
        return f'Directory({self.full_path}, p={self.parent}, size={self.total_size} children={self.children})'


def solution(lines):
    tot_lines = len(lines)
    cur_dir: Directory = None
    dir_name_stack:List[str] = []
    file_system: dict[str, Directory] = dict()
    ndx = 0
    while lines:
        line = lines.pop(0)
        print(f'PROCESSING {line} {tot_lines - len(lines)}')
        if line.startswith('$ cd '):
            new_dir = line[5:]
            if new_dir == '..':
                dir_name_stack.pop()
                # print(f'top of stack {dir_name_stack[-1]} ', end='')
                cur_dir = file_system['/'.join(dir_name_stack)]
                # print(f'cur_dir after a .. now {cur_dir}')
            else:
                cur_dir = Directory('/'.join(dir_name_stack + [new_dir]) , cur_dir.full_path if cur_dir is not None else None)
                dir_name_stack.append(new_dir)
                file_system[cur_dir.full_path] = cur_dir
                # print(f'changed dir into {cur_dir.rel_path}')
            # print(f'dir_stack={dir_name_stack}')
        elif line == '$ ls':
            print(f'SUB PROCESSING {line}  {tot_lines - len(lines)}')
            while lines and lines[0][0] != '$':
                line = lines.pop(0)
                print(f'SUB SUB PROCESSING {line}  {tot_lines - len(lines)}')
                if line.startswith('dir '):
                    print(f'I see dir {line[4:]}')
                    cur_dir.children.append(line[4:])
                else:
                    print(f'I see file {line}')
                    size, filename = line.split(' ')
                    cur_dir.children.append((size, filename))
                    print(f'adding {int(size)} to {cur_dir.full_path} for file {filename}')
                    cur_dir.total_size += int(size)
                    walk = cur_dir
                    while walk.parent is not None:
                        walk = file_system[walk.parent]
                        # print(f'adding {int(size)} to {walk.rel_path} for file {filename}')
                        walk.total_size += int(size)

    for dir_name in file_system:
        print(file_system[dir_name])
    part_1 = sum([directory.total_size for directory in file_system.values() if directory.total_size <= 100000])
    print(f'day 07 part 1: {part_1}')
    total_size = file_system['/'].total_size
    cur_free_space = 70000000 - total_size
    needed_size = 30000000 - cur_free_space
    print(f'total_size:{total_size} needed_size:{needed_size}')
    # return sorted([(directory.full_path, directory.total_size) for directory in file_system.values()], key=lambda x: x[1], reverse=True)
    # return [directory.total_size for directory in file_system.values() if directory.total_size >= needed_size]
    return sorted([directory.total_size for directory in file_system.values() if directory.total_size >= needed_size], reverse=True)[-1]


# def test_demo_input():
#     lines = list(open(f'{aoc_day_number}_demo.txt').read().splitlines())
#     assert solution([l for l in lines]) == 95437

#
# def test_part_1():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f'I got {len(lines)} lines')
#     print(f' day {aoc_day_number} part 1: {solution([l for l in lines])}', end='')


# def test_part_2():
#     lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
#     print(f' day {aoc_day_number} part 2: {solution(lines, execute_transfer=whole_stack)}', end='')
#

if __name__ == '__main__':
    # lines = list(open(f'{aoc_day_number}_demo.txt').read().splitlines())
    # assert solution([l for l in lines]) == 95437


    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f'I got {len(lines)} lines')
    print(f'day {aoc_day_number} part 2: {solution([l for l in lines])}', end='')
