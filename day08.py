import time, itertools, collections, math


def load(file):
  with open(file) as f:
    return [tuple(int(n) for n in zeile.split(',')) for zeile in f.read().split('\n')]


def entfernung(a, b):
  return abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2 + abs(a[2] - b[2]) ** 2


def solve(p):
  entf_map = [(entfernung(a, b), a, b) for a, b in itertools.combinations(p, 2)]
  point2circuit = dict()
  circuits = collections.defaultdict(set)

  c_id = 0
  for i, (_, a, b) in enumerate(sorted(entf_map)):
    if a not in point2circuit and b not in point2circuit:
      point2circuit[a] = c_id
      point2circuit[b] = c_id
      circuits[c_id] |= {a, b}
      c_id += 1
    elif a in point2circuit and b not in point2circuit:
      point2circuit[b] = point2circuit[a]
      circuits[point2circuit[a]] |= {b}
    elif b in point2circuit and a not in point2circuit:
      point2circuit[a] = point2circuit[b]
      circuits[point2circuit[b]] |= {a}
    elif a in point2circuit and b in point2circuit and point2circuit[a] != point2circuit[b]:
      new_id, old_id = point2circuit[a], point2circuit[b]
      circuits[new_id] |= circuits[old_id]
      for point in circuits[old_id]:
        point2circuit[point] = new_id
      del circuits[old_id]

    # Part 1
    if i == 999:
      top3 = sorted([len(c) for c in circuits.values()], reverse=True)[:3]
      p1 = math.prod(top3)

    # Part2
    if len(circuits) == 1 and len(p) == len(circuits[point2circuit[a]]):
      p2 = a[0] * b[0]
      break

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day08.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
