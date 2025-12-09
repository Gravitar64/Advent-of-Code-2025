import time, itertools, math


def load(file):
  with open(file) as f:
    return [tuple(int(n) for n in zeile.split(',')) for zeile in f.read().split('\n')]


def solve(p):
  entf_map = sorted(itertools.combinations(p,2), key=lambda x:math.dist(*x))
  circuits = {i : {pos} for i,pos in enumerate(p)}

  
  for i, (a, b) in enumerate(entf_map):
    for id,boxes in circuits.items():
      if a in boxes: id1=id
      if b in boxes: id2=id

    if id1 != id2:
      circuits[id1] |= circuits[id2]
      del circuits[id2]

    # Part 1
    if i == 999:
      top3 = sorted([len(c) for c in circuits.values()], reverse=True)[:3]
      p1 = math.prod(top3)

    # Part2
    if len(circuits) == 1:
      p2 = a[0] * b[0]
      break

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day08.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
