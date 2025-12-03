import time


def load(file):
  with open(file) as f:
    return f.read().split('\n')


def solve(p, länge, e=0):
  for banks in p:
    left, right, joltage, i = banks[:-länge], [*banks[-länge:]], '', -1
    while right:
      left = left[i + 1 :] + right.pop(0)
      i = left.index(max(left))
      joltage += left[i]
    e += int(joltage)
  return e


time_start = time.perf_counter()
p = load('day03.txt')
print(solve(p, 2), solve(p, 12))
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
