# Part2 by 4HbQ:
# https://www.reddit.com/r/adventofcode/comments/1pity70/comment/nt8vlv9/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import time, collections, scipy


def load(file):
  with open(file) as f:
    return [[e[1:-1] for e in zeile.split()] for zeile in f]


def bfs(target, buttons):
  q, seen = collections.deque([(0, 0)]), {0}
  while q:
    pressed, lights = q.popleft()
    if lights == target: return pressed
    for button in buttons:
      new_lights = lights ^ button
      if new_lights in seen: continue
      seen.add(new_lights)
      q.append((pressed + 1, new_lights))


def solve(p):
  p1 = p2 = 0
  b2int = lambda x: sum(1 << i for i in reversed(x))

  for lights, *buttons, joltages in p:
    light = b2int([i for i, c in enumerate(lights) if c == '#'])
    buttons = [[*map(int, b.split(','))] for b in buttons]
    joltages = [*map(int, joltages.split(','))]

    p1 += bfs(light, [b2int(b) for b in buttons])

    # The coefficients of the linear objective function to be minimized.
    coeff = [1] * len(buttons)
        
    # The equality constraint matrix. Each row of A_eq specifies the coefficients
    # of a linear equality constraint on x.
    ecm = [[i in b for b in buttons] for i in range(len(joltages))]

    # b_eq 1-D array
    # The equality constraint vector. Each element of A_eq @ x must equal the
    # corresponding element of b_eq.

    # Integrality
    # Indicates the type of integrality constraint on each decision
    # 1 : Integer variable; decision variable must be an integer within bounds.
    result = scipy.optimize.linprog(coeff, A_eq=ecm, b_eq=joltages, integrality=1)
    p2 += round(result.fun)
    
  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day10.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
