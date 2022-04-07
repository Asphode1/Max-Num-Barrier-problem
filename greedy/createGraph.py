import sys
sys.path.append('.')

from utils.Sensor import Sensor
from utils.distances import minNum

def createWeight(sensorList: list[Sensor], S: int, l: int, lr: float) -> list[int]:
  weight = [([None] * (S + 2)) for i in range(S + 2)]
  for i in range(S + 2):
    for j in range(S + 2):
      if((i == 0 and j == S + 1) or (i == S + 1 and j == 0)):
        weight[i][j] = -1
      else:
        weight[i][j] = minNum(sensorList, i, j, S, l, lr)
  return weight
