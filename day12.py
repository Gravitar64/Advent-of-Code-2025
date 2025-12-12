import time, collections


def load(file):
  with open(file) as f:
    return [[zeile for zeile in block.split('\n')] for block in f.read().split('\n\n')]


def get_xy(space):
  coord = {(x,y) for y,z in enumerate(space) for x,c in enumerate(z) if c == '#'}
  return len(coord), coord


def to_big(region,ids,presents):
  size_shapes = sum(presents[i][0] * n for i,n in enumerate(ids))
  return size_shapes > region


def precalculate(presents):
  for id,(size,shape) in presents.items():
    shapes = set()
    for _ in range(4):
      rot=set()
      for x,y in shape:
        x,y=x-1,y-1
        x,y=-y,x
        x,y=x+1,y+1
        rot.add((x,y))
      shapes.add(frozenset(rot))
      flip_ver = {(2-x,y) for x,y in rot}
      shapes.add(frozenset(flip_ver))
      flip_hor = {(x,2-y) for x,y in rot}
      shapes.add(frozenset(flip_hor))
      shape = rot
    presents[id]= size, shapes
  return presents        


def print_shape(shape):
  for y in range(3):
    print()
    for x in range(3):
      if (x,y) in shape: 
        print('#',end='')
      else:
        print('.',end='')
  print()


def bfs(width,height,ids,presents):
  free = set((x,y) for x in range(width) for y in range(height))
  q = collections.deque([(free,ids)])
  while q:
    free, ids = q.pop()
    if sum(ids) == 0: return True
    for i,id in enumerate(ids):
      if id == 0: continue
      for shape in presents[i][1]:
        for dx,dy in free:
          transform = {(x+dx,y+dy) for x,y in shape}
          if not transform.issubset(free): continue
          new_ids = ids[:]
          new_ids[i] -= 1
          q.append((free-transform,new_ids))


def solve(p):
  p1 = 0
  presents = {int(pr[0][:-1]): get_xy(pr[1:]) for pr in p[:-1]}
  presents = precalculate(presents)
  for space in p[-1]:
    dim,*ids = space.split()
    width,height = map(int,dim[:-1].split('x'))
    region = width * height
    ids = [*map(int,ids)]
    if to_big(region,ids,presents): continue
    p1 += bfs(width, height, ids, presents)
    print(p1)
    
  return p1  


time_start = time.perf_counter()
print(f'Solution: {solve(load("day12.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
