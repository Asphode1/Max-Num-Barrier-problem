import sys
sys.path.append('.')

from math import ceil, floor
from random import randint

from ga.Population import Population

def crossover(p1: Population, p2: Population, rate: int) -> Population:
  l = p1.length
  crossLen = randint(floor(l / 3), ceil(l * 2 / 3))
  child = Population(l)
  data = [None] * l
  index = [None] * l
  startPos = randint(0, l - crossLen - 1)
  for i in range(startPos, startPos + crossLen):
    data[i] = p1.data[i]
    index[i] = p1.index[i]
  i = 0
  j = 0
  while(i < startPos):
    if(i in data):
      i += 1
    else:
      data[j] = p2.data[i]
      index[j] = p2.index[j]
      i += 1
      j += 1
  j = startPos + crossLen
  for ind in range(i, l):
    if(p2.data[ind] in data):
      continue
    else:
      data[j] = p2.data[ind]
      index[j] = p2.index[ind]
      j += 1
  child.update(data, index)
  child.mutation(rate)
  return child
