import sys
sys.path.append('.')

from greedy.Graph import BG
from utils.Sensor import Sensor, SortedSensor

class Population:
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
  def mutation(self, lst: list[SortedSensor], rate: int):

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
