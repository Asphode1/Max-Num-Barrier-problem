import sys
sys.path.append('.')

from random import randint, random

from utils.Sensor import SortedSensor

class Population:
  length = 0
  data = []
  index = []
  fitness = 0

  def __init__(self, n: int) -> None:
    self.length = n
    for i in range(n):
      self.data.append(i)
      self.index.append(0)

  def update(self, data: list[int], index: list[int]):
    self.data = data
    self.index = index
    return self

  def mutation(self, rate: int):
    rnd = random()
    if(rnd <= rate / 2):
      rnd1 = randint(0, self.length - 1)
      rnd2 = randint(0, self.length - 1)
      tmp = self.data[rnd1]
      self.data[rnd1] = self.data[rnd2]
      self.data[rnd2] = tmp
    if(rnd > rate / 2 and rnd <= rate):
      rndi = randint(0, self.length - 1)
      self.index[rndi] = int(not self.index[rndi])
    return self

  def start(self, delta: float, arr: list[SortedSensor]):
    return self
