# solution to https://adventofcode.com/2022/day/7
from typing import Tuple, List

aoc_day_number = '07'

class Directory:
    def __init__(self, full_path: str, parent: str = None):
        self.full_path = full_path
        self.parent = parent
        self.total_size = 0


    def __repr__(self):
        return f'Directory({self.full_path}, p={self.parent}, size={self.total_size})'


def solution(lines):
    tot_lines = len(lines)
    cur_dir: Directory = None
    dir_name_stack:List[str] = []
    filesys: dict[str, Directory] = dict()
    ndx = 0
    while lines:
        line = lines.pop(0)
        if line.startswith('$ cd '):
            new_dir = line[5:]
            if new_dir == '..':
                dir_name_stack.pop()
                cur_dir = filesys['/'.join(dir_name_stack)]
            else:
                cur_dir = Directory('/'.join(dir_name_stack + [new_dir]) , cur_dir.full_path if cur_dir is not None else None)
                dir_name_stack.append(new_dir)
                filesys[cur_dir.full_path] = cur_dir
        elif line == '$ ls':
            while lines and lines[0][0] != '$':
                line = lines.pop(0)
                if not line.startswith('dir '):
                    size, filename = line.split(' ')
                    cur_dir.total_size += int(size)
                    walk = cur_dir
                    while walk.parent is not None:
                        walk = filesys[walk.parent]
                        walk.total_size += int(size)

    part_1 = sum([d.total_size for d in filesys.values() if d.total_size <= 100000])
    print(f'day 07 part 1: {part_1}')
    needed_size = 30000000 - (70000000 - filesys['/'].total_size)
    return sorted([d.total_size for d in filesys.values() if d.total_size >= needed_size], reverse=True)[-1]

if __name__ == '__main__':
    lines = list(open(f'{aoc_day_number}.txt').read().splitlines())
    print(f'day {aoc_day_number} part 2: {solution([l for l in lines])}', end='')
