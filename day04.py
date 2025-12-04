import time


def load(file):
  with open(file) as f:
    return {(x, y) for y, zeile in enumerate(f.read().split('\n')) 
            for x, c in enumerate(zeile) if c == '@'}


def nachbarn(x, y, p):
  nachbarn = {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
              (x + 1, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1)}
  return p & nachbarn


def solve(p):
  
  p1 = sum(len(nachbarn(x, y, p)) < 4 for x,y in p)
  
  p2 = 0
  while True:
    remove_rolls = set()
    
    for x, y in p:
      if len(nachbarn(x, y, p)) > 3: continue
      remove_rolls.add((x, y))
    
    if not remove_rolls: break
    p2 += len(remove_rolls)
    p -= remove_rolls

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day04.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
