import sys
sys.path.append('.')

from random import randint, random

from ga.crossover import crossover
from ga.create import createParent
from ga.fitness import fitness
from ga.parentSelect import parentSelect
from ga.Population import Population
from utils.Sensor import SortedSensor


def shuffle(lst: list) -> list:
  l = len(lst)
  newlst = lst.copy()
  for i in newlst:
    rnd = int(randint(0, l - 1))
    tmp = i
    i = lst[rnd]
    lst[rnd] = tmp
  return newlst

def naturalSelection(pop: list[Population], size) -> list[Population]:
  lst = sorted(pop, key=lambda x: x.fitness)
  l = size / 2
  return shuffle(lst[0:int(l)])

def getBestChild(pop: list[Population]) -> Population:
  lst = sorted(pop, key=lambda x: x.fitness, reverse=True)
  return lst[0]

def ga(sSens: list[SortedSensor], s: int, m: int, a: float, r: int, l: int, lr: float, mutationRate: float, gen: int, size: int, crossRate: float, delta: float) -> list[Population]:
  parents = createParent(sSens, s, m, a, r, size, l, lr, delta)
  count = 0
  while(count < gen):
    parents = naturalSelection(parents, size)
    while(len(parents) < size):
      p = parentSelect(parents)
      rnd = random()
      if(rnd < crossRate):
        child = crossover(p[0], p[1], mutationRate)
        child.fitness = fitness(child, sSens, s, m, a, r, l, lr)
        parents.append(child)
    parents = shuffle(parents)
    count += 1
  return parents
