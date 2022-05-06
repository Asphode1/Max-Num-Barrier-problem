import sys
sys.path.append('.')

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
      self.data.append(path)
      sensorGraph.removePath(path)
      k += 1
    return self
