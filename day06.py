import time, re, math


def load(file):
  with open(file) as f:
    return f.read().split('\n')


def solve(p):
  p1 = p2 = 0
  zahlen, operators = p[:-1], re.findall('[*+] +',p[-1])
  
  left = 0
  for op in operators:
    spalte = [z[left:left+len(op)] for z in zahlen]
    stellen = [''.join(s).replace(' ','') for s in zip(*spalte)]
    stellen = [s for s in stellen if s.isnumeric()]
    
    operator = op[0]
    if operator == '*':
      p1 += math.prod(map(int,spalte))
      p2 += math.prod(map(int,stellen))
    else:
      p1 += sum(map(int,spalte))
      p2 += sum(map(int,stellen))
    left += len(op)
  
  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day06.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
