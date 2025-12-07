import time, re, math


def load(file):
  with open(file) as f:
    return [[c for c in zeile] for zeile in f.read().split('\n')] 


def solve(p):
  p1 = p2 = 0
  beams = {p[0].index('S')}
  for zeile in p[1:]:
    new_beams = set()
    for beam in beams:
      if zeile[beam] == '.': 
        new_beams.add(beam)
        continue
      new_beams.update({beam-1,beam+1})
      p1 += 1
    p2 += len(new_beams)
    beams = new_beams  
  return p1,p2    





time_start = time.perf_counter()
print(f'Solution: {solve(load("day07.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
