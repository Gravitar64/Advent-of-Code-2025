import time


def load(file):
  with open(file) as f:
    rng, ing = f.read().split('\n\n')
    ranges = [list(map(int, zeile.split('-'))) for zeile in rng.split('\n')]
    ingred = [int(n) for n in ing.split('\n')]
    return ranges, ingred


def solve(p):
  ranges, ingred = p
  p1 = sum(any(start <= ingr <= ende for start, ende in ranges) for ingr in ingred)

  p2 = ende_max = 0
  for start, ende in sorted(ranges):
    start = max(start, ende_max + 1)
    p2 += max(0, ende - start + 1)
    ende_max = max(ende_max, ende)

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day05.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
