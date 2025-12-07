import time


def load(file):
  with open(file) as f:
    return [[i for i, c in enumerate(zeile) if c != '.'] for zeile in f.read().split('\n')]


def solve(p):
  p1 = p2 = 0
  beams = [0] * 16
  beams[p.pop(0)[0]] = 1
  print(beams)

  for zeile in p:
    for splitter in zeile:
      if not beams[splitter]: continue
      p1 += 1
      beams[splitter - 1] += beams[splitter]
      beams[splitter + 1] += beams[splitter]
      beams[splitter] = 0
    #if zeile: print(beams)
  p2 += sum(beams)

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day07.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
