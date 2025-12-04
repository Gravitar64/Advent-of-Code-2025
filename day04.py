import time


def load(file):
  with open(file) as f:
    return {(x,y) for y,zeile in enumerate(f.read().split('\n')) 
                  for x,c in enumerate(zeile) if c == '@'}


def nachbarn(x,y,p):
  nachbarn = {(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y-1), (x-1, y+1), (x+1, y-1)}
  return p & nachbarn



def solve(p):
  p1 = p2 = 0
  for x,y in p:
    p1 += len(nachbarn(x,y,p)) < 4
  
  while True:
    änderungen = False
    rolls = set()
    for x,y in p:
      if len(nachbarn(x,y,p)) < 4:
        rolls.add((x,y))
        p2 += 1
        änderungen = True
    p -= rolls    
    if not änderungen: break

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day04.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
