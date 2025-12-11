import time


def load(file):
  with open(file) as f:
    return [[e[1:-1] for e in zeile.split()] for zeile in f]


def bfs(target, buttons):
  queue, seen = [[0]], {0}
  while queue:
    path = queue.pop(0)
    lights = path[-1]
    if lights == target: return len(path) - 1
    for button in buttons:
      new_lights = lights ^ button
      if new_lights in seen: continue
      seen.add(new_lights)
      queue.append(path + [new_lights])


  

def solve(p):
  p1 = p2 = 0
  b2i = lambda x: sum(2**i for i in reversed(x))
  
  for lights, *buttons, joltages in p:
    light = b2i([i for i,c in enumerate(lights) if c == '#'])
    buttons = [b2i([int(n) for n in b.split(',')]) for b in buttons]
    joltages = tuple(int(n) for n in joltages.split(','))
    p1 += bfs(light, buttons)
  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day10.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
