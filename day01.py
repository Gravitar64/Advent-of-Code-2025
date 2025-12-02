import time


def load(file):
  with open(file) as f:
    return [(line[0], int(line[1:])) for line in f.readlines()]


def solve(p):
  p1 = p2 = 0

  pos = 50
  for richtung, anzahl in p:
    neue_pos = pos + anzahl if richtung == 'R' else pos - anzahl
    durchläufe, neue_pos = divmod(neue_pos,100)
    p1 += neue_pos == 0
    
    if neue_pos == 0 and durchläufe > 0: durchläufe -= 1
    if pos == 0 and durchläufe < 0:      durchläufe += 1
    p2 += abs(durchläufe)
    
    pos = neue_pos

  return p1, p1 + p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day01.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
