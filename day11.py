#Solution by 4HbQ
#https://www.reddit.com/r/adventofcode/comments/1pjp1rm/comment/ntf4e0t/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import time, functools


def load(file):
  with open(file) as f:
    return [zeile.split() for zeile in f]


@functools.cache
def count(node, target):
  return node == target or \
         sum(count(next,target) for next in devices[node])


def solve():
  p1 = count('you','out')
  p2 = count('svr','fft') * count('fft','dac') * count('dac','out')
  
  return p1, p2


time_start = time.perf_counter()
p = load("day11.txt")
devices = {node[:-1]:outputs for node, *outputs in p} | {'out':[]}


print(f'Solution: {solve()}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
