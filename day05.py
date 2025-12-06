import time


def load(file):
  with open(file) as f:
    rng, ing = f.read().split('\n\n')
    ranges = [list(map(int, zeile.split('-'))) for zeile in rng.split('\n')]
    ingred = [int(n) for n in ing.split('\n')]
    return ranges, ingred


def solve(p):
  ranges, ingredients = p
  p1 = sum(any(start <= ingr <= ende for start, ende in ranges) for ingr in ingredients)

  ranges.sort()
  new_ranges = [ranges.pop(0)]
  for start, ende in ranges:
    last_ende = new_ranges[-1][1]
    if start > last_ende:
      new_ranges.append([start, ende])
    elif ende > last_ende:
      new_ranges[-1][1] = ende
  p2 = sum(ende - start + 1 for start, ende in new_ranges)

  # p2 = last_ende = 0
  # for start, ende in ranges:
  #   start = max(start, last_ende+1)
  #   p2 += max(0, ende-start+1)
  #   last_ende = max(ende, last_ende)


  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day05.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
