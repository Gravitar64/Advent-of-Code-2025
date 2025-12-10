import time


def load(file):
  with open(file) as f:
    return [zeile.split() for zeile in f.read().split('\n')]


def zustandsänderung(state, button):
  for n in button:
    state[n] = '1' if state[n] == '0' else '0'
  return state   


def bfs(ziel, buttons):
  start = ['0']*len(ziel)
  queue, seen = [[start]], {tuple(start)}
  while queue:
    pfad = queue.pop(0)
    akt_zustand = pfad[-1]
    if akt_zustand == ziel: return len(pfad)-1
    for button in buttons:
      neu_zustand = zustandsänderung(akt_zustand[:], button)
      if (s:=tuple(neu_zustand)) in seen: continue
      seen.add(s)
      queue.append(pfad+[neu_zustand])


def solve(p):
  p1 = p2 = 0
  for i,machine in enumerate(p):
    lights = ['1' if c == '#' else '0'for c in machine[0][1:-1]]
    buttons = [[int(n) for n in button[1:-1].split(',')] for button in machine[1:-1]]
    joltages = [int(n) for n in machine[-1][1:-1].split(',')]
    p1 += bfs(lights, buttons)
           
  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day10.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
