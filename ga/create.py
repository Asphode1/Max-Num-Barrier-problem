import sys
sys.path.append('.')

from ga.fitness import fitness
from ga.Population import Population
from utils.Sensor import SortedSensor

def createParent(sens: list[SortedSensor], s: int, m: int, a: float, r: int, size: int, l: int, lr: int) -> list[Population]:
  parents = [Population(s)] * size
  for i in range(size):
    parents[i].start(l / s * 10, sens)
    parents[i].fitness = fitness(parents[i], sens, s, m, a, r, l, lr)
  return parents
