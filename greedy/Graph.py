import sys
sys.path.append('.')

from math import inf
from random import shuffle

from utils.Sensor import SortedSensor
from utils.distances import strongDist

class WBG:
  def __init__(self, v: int, weight: list[list[int]]):
    self.vertex = v
    self.weight = weight
    edge = [None] * v
    for i in range(v):
      edge[i] = [0] * v
    self.edge = edge

  def addEdge(self, v1: int, v2: int):
    self.edge[v1][v2] = 1
    self.edge[v2][v1] = 1
    return self

  def updateEdge(self, edge: list[list[int]]):
    self.edge = edge.copy()
    return self

  def removeEdge(self, v1: int, v2: int):
    self.edge[v1][v2] = 0
    self.edge[v2][v1] = 0
    return self

  def removePath(self, p: list[int]):
    for i in range(1, len(p) - 1):
      self.edge[p[i]] = [0] * self.vertex
    return self

  def resetGraph(self):
    edge = [None] * self.vertex
    for i in range(self.vertex):
      edge[i] = [1] * self.vertex
      edge[i][i] = 0
    edge[0][self.vertex - 1] = 0
    edge[self.vertex - 1][0] = 0
    self.edge = edge
    return self

  def recurDfs(self, v: int, visited: list[int], path: list[int]) -> None:
    visited[v] = True
    path.append[v]
    for i in range(self.vertex):
      n = self.edge[v][i]
      if((not visited[i]) and n != 0):
        self.recurDfs(i, visited, path)

  def DFS(self, v: int) -> list[int]:
    path = []
    visited = [False] * self.vertex
    self.recurDfs(v, visited, path)
    return path

  def BFS(self, v: int) -> list[int]:
    visited = [False] * self.vertex
    path = []
    visited[v] = True
    queue = [v]
    while(len(queue) > 0):
      s = queue.pop(0)
      path.append(s)
      for i in range(self.vertex):
        n = self.edge[s][i]
        if(n != 0 and (not visited[i])):
          queue.append(i)
          visited[i] = True
    return path

  def checkPath(self, s: int, t: int) -> bool:
    visited = [False] * self.vertex
    queue = [s]
    visited[s] = True
    while(len(queue) > 0):
      n = queue.pop(0)
      if(n == t):
        return True
      for i in range(self.vertex):
        if(visited[i] == False and self.edge[n][i] == 1):
          queue.append(i)
          visited[i] = True
    return False

  def findLT(self) -> int:
    visited = [False] * self.vertex
    count = 0
    while(False in visited):
      a = visited.index(False)
      self.recurDfs(a, visited, [])
      count += 1
    return count

  def dijkstra(self, s: int, t: int) -> list:
    dist = [inf] * self.vertex
    dist[s] = 0
    prev = [None] * self.vertex
    set = [i for i in range(self.vertex)]
    while(len(set)):
      min = inf
      ind = -1
      for v in range(self.vertex):
        if(v in set and dist[v] <= min):
          min = dist[v]
          ind = v
      u = ind
      set.remove(u)
      if(u == t):
        break
      for i in range(self.vertex):
        if(self.edge[u][i] != 0 and (i in set)):
          alt = dist[u] + self.weight[u][i]
          if(alt < dist[i]):
            dist[i] = alt
            prev[i] = u
    path = []
    tmp = t
    if(prev[tmp] != None or u == s):
      while(tmp != None):
        path.insert(0, tmp)
        tmp = prev[tmp]
    return [path, dist[t]]

class BG(WBG):
  def __init__(self, v: int):
    self.vertex = v
    edge = [None] * v
    for i in range(v):
      edge[i] = [0] * v
    self.edge = edge

  def initEdge(self, sensors: list[SortedSensor], maxDist: float, S: int, L: int):
    for i in range(self.vertex - 1):
      for j in range(i + 1, self.vertex):
        if not(i == 0 and j == S + 1):
          if(strongDist(sensors, i, j, S, L) <= maxDist):
            self.edge[i][j] = 1
    return self

  def getNeighbors(self, s: int) -> list[int]:
    nb = []
    for i in range(self.vertex):
      if(self.edge[i][s] != 0):
        nb.append(i)
    shuffle(nb)
    return nb

  def recurRDFS(self, v: int, visited: list[int], path: list[int]) -> None:
    visited[v] = True
    path.append(v)
    nb = self.getNeighbors(v)
    for i in range(len(nb)):
      if(not visited[nb[i]]):
        self.recurRDFS(nb[i], visited, path)

  def randomizedDFS(self, v: int) -> list[int]:
    path = []
    visited = [False] * self.vertex
    self.recurRDFS(v, visited, path)
    return path

  def findPathRecurRDFS(self, s: int, t: int, visited: list[int], before: list[int]) -> int:
    visited[t] = True
    if(s != t):
      nb = self.getNeighbors(t)
      for i in range(len(nb)):
        if(not visited[nb[i]]):
          before[t] = nb[i]
          return self.findPathRecurRDFS(s, nb[i], visited, before)
      return 0
    return 1

  def findPathRDFS(self, s: int, t: int) -> list[int]:
    visited = [False] * self.vertex
    before = [None] * self.vertex
    self.findPathRecurRDFS(s, t, visited, before)
    tmp = s
    path = [s]
    while(tmp != t):
      if(tmp in before):
        path.append(before.index(tmp))
        tmp = before.index(tmp)
      else:
        break
    return path
