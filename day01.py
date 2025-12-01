import time, collections


def load(file):
  with open(file) as f:
    return [(line[0], int(line[1:])) for line in f.readlines()]


def solve(p):
  position = 50
  p1 = p2 = 0

  for richtung, anzahl in p:
    position = (position + anzahl) % 100 if richtung == 'R' else (position - anzahl) % 100
    p1 += position == 0

  # position = collections.deque(range(100))
  # position.rotate(-50)
  # for richtung, anzahl in p:
  #   if richtung == 'R':
  #     for _ in range(anzahl):
  #       position.rotate(1)
  #       p2 += position[0] == 0
  #   else:
  #     for _ in range(anzahl):
  #       position.rotate(-1)
  #       p2 += position[0] == 0

  position = 50
  for richtung, anzahl in p:
    durchläufe, new_pos = divmod(position+anzahl,100) if richtung == 'R' else divmod(position-anzahl,100)
    p2 += new_pos == 0
    if new_pos == 0 and durchläufe > 0: durchläufe -= 1
    if position == 0 and durchläufe < 0: durchläufe += 1
    p2 += abs(durchläufe)
    position = new_pos

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day1.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
