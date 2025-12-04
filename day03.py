import time


def load(file):
  with open(file) as f:
    return f.read().split('\n')


def solve(p, länge, e=0):
  for banks in p:
    suchbereich, reserve, joltage, i = banks[:-länge], [*banks[-länge:]], '', -1
    while reserve:
      suchbereich = suchbereich[i + 1:] + reserve.pop(0)
      i = suchbereich.index(max(suchbereich))
      joltage += suchbereich[i]
    e += int(joltage)
  return e


time_start = time.perf_counter()
p = load('day03.txt')
print(solve(p, 2), solve(p, 12))
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
