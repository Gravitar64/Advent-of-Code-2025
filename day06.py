import time, re, math


def load(file):
  with open(file) as f:
    raw = f.readlines()
    zahlen = [re.findall('\d+', zeile) for zeile in raw[:-1]]
    operators = raw[-1].replace(' ', '')
    return zahlen, operators


def solve(p):
  p1 = p2 = 0
  zahlen, operators = p

  for i, z in enumerate(zip(*zahlen)):
    if operators[i] == '*':
      p1 += math.prod(map(int, z))
    else:
      p1 += sum(map(int, z))

  for i1, z in enumerate(zip(*zahlen)):
    max_l = max(len(n) for n in z)
    for i2, n in enumerate(z):
      z = list(z)
      if len(n) < max_l:
        z[i2] = '.' * (max_l - len(n)) + n
    for stellen in zip(*z):
      print(stellen)
    print()

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day06.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
