import time


def load(file):
  with open(file) as f:
    return [[e[1:-1] for e in zeile.split()] for zeile in f]


def bfs(target, buttons):
  queue, seen = [(0,0)], {0}
  while queue:
    pressed, lights = queue.pop(0)
    if lights == target: return pressed
    for button in buttons:
      new_lights = lights ^ button
      if new_lights in seen: continue
      seen.add(new_lights)
      queue.append((pressed+1, new_lights))


def get_joltage(state,button,anz):
  for i in button:
    state[i] += anz
  return state  


def part2(target, buttons):
  state = [0]*len(target)
  queue, seen = [(0,state)], {tuple(state)}
  while queue:
    pressed, state = queue.pop(0)
    if state == target: return pressed
    for anz,i in sorted([(min(target[n]-state[n] for n in b),i) for i,b in enumerate(buttons)]):
      if anz < 0: 
        print(anz,i)
        continue
      for ad in range(anz,0,-1):
        new_state = get_joltage(state[:],buttons[i],ad)
        #if any(a > b for a,b in zip(new_state,target)): break
        if tuple(new_state) in seen: continue
        seen.add(tuple(new_state))
        queue.append((pressed+ad, new_state))
      
  

def solve(p):
  p1 = p2 = 0
  b2int = lambda x: sum(1<<i for i in reversed(x))
  
  for lights, *buttons, joltages in p:
    t1 = time.perf_counter()
    light = b2int([i for i,c in enumerate(lights) if c == '#'])
    buttons = [[int(n) for n in b.split(',')] for b in buttons]
    joltages = [int(n) for n in joltages.split(',')]
    p1 += bfs(light, [b2int(b) for b in buttons])
    p2 += (e:=part2(joltages, buttons))
    print(f'{e} {time.perf_counter()-t1:.2f} Sek.')
  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day10.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
