import sys
sys.path.append('.')

from math import sqrt
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
      self.data.append(i + 1)
      self.index.append(0)
    self.index[-1] = 1
    return self

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

  def start(self, lstSensor: list[SortedSensor]):
    l = len(lstSensor)
    lst = lstSensor.copy()
    start = []
    index = [i for i in range(0, l)]
    leftSensor = lst[0:10]
    lst = lst[10::1]
    while(len(index)):
      while(len(leftSensor)):
        rnd = randint(0, len(leftSensor) - 1)
        current = leftSensor[rnd]
        leftSensor.remove(current)
        next = []
        while(len(next) < 10):
          return
