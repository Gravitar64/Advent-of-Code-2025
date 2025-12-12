import time


def load(file):
  with open(file) as f:
    return [block.split('\n') 
            for block in f.read().
            replace('x', ' ').
            replace(':', '').
            split('\n\n')][-1]


def solve(p):
  regions = [[*map(int,r.split())] for r in p]
  return sum(w//3 * h//3 >= sum(ids) for w, h, *ids in regions)


time_start = time.perf_counter()
print(f'Solution: {solve(load("day12.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
