import sys
sys.path.append('.')

from ga.fitness import fitness
from ga.Population import Individua
from utils.Sensor import SortedSensor

def createParent(sens: list[SortedSensor], s: int, m: int, a: float, r: int, size: int, l: int, lr: int, delta: float) -> list[Individua;]:
  parents = [Individua
             (s)] * size
  for i in range(size):
    parents[i].start(delta, sens)
    parents[i].fitness = fitness(parents[i], sens, s, m, a, r, l, lr)
  return parents
