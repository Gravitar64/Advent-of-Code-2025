import time, re


def load(file):
  with open(file) as f:
    return re.findall('\d+', f.read())


def solve(p):
  pass


time_start = time.perf_counter()
print(f'Solution: {solve(load("day01.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
