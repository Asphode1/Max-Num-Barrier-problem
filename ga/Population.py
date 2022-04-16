import sys
sys.path.append('.')

from math import sqrt
from random import randint, random
from greedy.Graph import BG
from utils.Sensor import Sensor, SortedSensor

class Population:
  length = 0
  data = []
  fitness = 0

  def __init__(self, n: int) -> None:
    self.length = n

  def update(self, data: list[int]):
    self.data = data
    return self

  # TODO: change mutation algorithm
  def mutation(self, rate: int):

    return self

  def start(self, lstSensor: list[SortedSensor] | list[Sensor], maxDist: float):
    l = len(lstSensor)
    sensorGraph = BG(l + 2)
    sensorGraph.initEdge(lstSensor, maxDist)
