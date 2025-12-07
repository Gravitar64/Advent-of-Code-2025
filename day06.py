import time, re, math


def load(file):
  with open(file) as f:
    return f.read().split('\n')


def solve(p):
  p1 = p2 = 0
  zahlen, operators = p[:-1], re.findall('[*+] +',p[-1])
  operators[-1] += ' '  
  
  left = 0
  for op in operators:
    spalte =  [z[left:left+len(op)-1] for z in zahlen]
    stellen = [int(''.join(s)) for s in zip(*spalte)]
    spalte = map(int,spalte)
    
    p1 += math.prod(spalte) if op[0] == '*' else sum(spalte)
    p2 += math.prod(stellen) if op[0] == '*' else sum(stellen)
    
    left += len(op)
  
  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day06.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
