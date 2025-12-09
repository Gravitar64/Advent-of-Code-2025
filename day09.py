import time, itertools, shapely


def load(file):
  with open(file) as f:
    return [tuple(map(int,zeile.split(','))) for zeile in f]


def fläche(x1,y1,x2,y2):
  return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def solve(p):
  p1 = p2 = 0

  poly = shapely.Polygon(p)
  for (x1,y1), (x2,y2) in itertools.combinations(p, 2):
    f = fläche(x1,y1,x2,y2)
    p1 = max(p1, f)

    if f < p2: continue
    rect = shapely.box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    if poly.contains(rect):
      p2 = max(p2, f)

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day09.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
