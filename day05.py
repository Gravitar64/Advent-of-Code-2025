import time


def load(file):
  with open(file) as f:
    rng, ing = f.read().split('\n\n')
    ranges = [list(map(int,zeile.split('-'))) for zeile in rng.split('\n')]
    ingred = [int(n) for n in ing.split('\n')]
    return ranges, ingred


def solve(p):
  ranges, ingred = p
  p1 = sum(any(start <= ingr <= ende for start, ende in ranges) for ingr in ingred)

  #Für die Zählung der Ranges gibt es 3 Fälle:
  #1. Fall: Komplett eigenständiger Bereich ohne Überschneidung
  #-> dann p2 um ende-start+1 erhöhen
  
  #2. Fall: Die vorherige Range ragt in die nachfolgende Range hinein
  #-> dann den Startwert der nachfolgenden Range auf den Endwert der vorhergehenden
  #   Range +1 setzen, danach dann wieder p2 um ende-start+1 erhöhen
  
  #3. Fall: die aktuelle Range wird komplett von der vorherigen überdeckt
  #-> dann darf p2 nicht verändert werden
  #   erreicht wird dies durch max(0, ende-start+1) da in diesem Fall start > ende
  #   ist, da der startwert der aktuellen Range ja auf das max(ende,ende_max) der
  #   vorherigen range gesetzt wird
  
  p2 = ende_max = 0
  for start, ende in sorted(ranges):
    start = max(start, ende_max + 1)
    p2 += max(0, ende - start + 1) 
    ende_max = max(ende_max, ende)

  return p1, p2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day05.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
