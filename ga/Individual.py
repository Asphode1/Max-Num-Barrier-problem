import sys
sys.path.append('.')

from random import random, sample

from greedy.Graph import BG
from utils.Sensor import Sensor, SortedSensor
from ga.fitness import getBarrier
class Individual:
  length = 0
  data = []
  index = []
  fitness = 0

  def __init__(self, n: int) -> None:
    self.length = n

  def update(self, data: list[int], index: list[int]):
    self.data = data.copy()
    self.index = index.copy()
    return self

  # TODO: change mutation algorithm
  def mutation(self, lst: list[SortedSensor], crossRate: float, numberRate: float, typeRate: float):
    rnd1 = random()
    if(rnd1 < typeRate):
      """cross barrier mutation"""
      barriers = getBarrier(self)
      rnd2 = random()
      if(rnd2 < numberRate):
        n = 2
        count = 0
        crossBarrier = sample(barriers, 4)
    return self

  # TODO: optimize sensorGraph
  def start(self, graph: BG, maxK: int, S: int):
    sensorGraph = BG(S + 2)
    sensorGraph.updateEdge(graph.edge)
    k = 0
    while(k < maxK):
      path = sensorGraph.findPathRDFS(0, sensorGraph.vertex - 1)
      if(len(path) == 0):
        break
      for i in path:
        self.data.append(i)
        self.index.append(k)
      sensorGraph.removePath(path)
      k += 1
    return self
