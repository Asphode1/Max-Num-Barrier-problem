import sys
sys.path.append('.')

from math import ceil, floor

from utils.distances import minNum
from utils.Sensor import SortedSensor
from ga.Population import Population

def fitness(ind: Population, sensors: list[SortedSensor], s: int, m: int, a: float, r: int, l: int, lr: float) -> int:
  LIM = ceil(l / lr)
  k = 0
  barriers = []
  i = 0
  index = 0
  prevIndex = 0
  barrier = []
  while(i < len(sensors)):
    index = ind.index[i]
    if(index == prevIndex):
      barrier.append(ind.data[i])
      i += 1
    else:
      prevIndex = index
      barriers.append(barrier)
      barrier = []
      i += 1
  totalCost = 0
  costs = []
  for barrier in barriers:
    cost = minNum(sensors, 0, barrier[0], s, a, r, l, lr)
    for i in range(len(barrier) - 1):
      cost += minNum(sensors, barrier[i], barrier[i + 1], s, a, r, l, lr)
    cost += minNum(sensors, barrier[len(barrier) - 1], s + 1, s, a, r, l, lr)
    costs.append(cost)
  costs.sort()
  for i in costs:
    totalCost += i
    if(totalCost <= m):
      k += 1
    else:
      break
  left = m - totalCost
  return k + floor(left / LIM)
