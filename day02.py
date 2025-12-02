import time, re


def load(file):
  with open(file) as f:
    return [tuple(map(int,range.split('-'))) for range in f.read().split(',')]


def solve(p):
  p1 = p2 = 0
  for start, ende in p:
    for wert in range(start,ende+1):
      w = str(wert)
      if re.findall(r'^(\d+)\1$',w):  p1 += wert
      if re.findall(r'^(\d+)\1+$',w): p2 += wert
  return p1,p2   
  



time_start = time.perf_counter()
print(f'Solution: {solve(load("day02.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
