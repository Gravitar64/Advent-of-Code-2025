#Based on an idea from 4HbQ
#https://www.reddit.com/r/adventofcode/comments/1pkje0o/comment/ntlkg9i/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import time, re


def load(file):
  with open(file) as f:
    return [[*map(int,re.findall('\d+',r))] 
             for r in f.readlines()[30:]]


def solve(p):
  return sum(w//3*h//3 >= sum(ids) for w,h,*ids in p)

time_start = time.perf_counter()
print(f'Solution: {solve(load("day12.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
