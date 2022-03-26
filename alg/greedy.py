import sys
sys.path.append('.')

from math import ceil, floor

from greedy.Graph import WBG

def greedy(graph: WBG, S: int, M: int, l: int, lr: float) -> int:
  LIM = ceil(l / lr)
  passed = []
  q = 0
  totalCost = 0
  while True:
    if(graph.checkPath(0, S + 1)):
      [path, cost] = graph.dijkstra(0, S + 1)
      if(cost < LIM):
        if(totalCost + cost < M):
          q += 1
          path.pop(0)
          del path[-1]
          for i in path:
            passed.append(i)
          totalCost += cost
          graph.removePath(path)
        elif(totalCost + cost == M):
          return q + 1
        else:
          return q
      else:
        return q + floor((M - totalCost) / LIM)
    else:
      return q + floor((M - totalCost) / LIM)
