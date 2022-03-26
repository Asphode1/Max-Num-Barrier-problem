import sys
sys.path.append('.')

from utils.Sensor import Sensor
from utils.distances import minNum

def createWeight(sensorList: list[Sensor], S: int, A: float, R: int, l: int, lr: float) -> list[int]:
  weight = [None] * (S + 2)
  for i in range(S + 2):
    weight[i] = [None] * (S + 2)
  for i in range(S + 2):
    for j in range(S + 2):
      weight[i][j] = minNum(sensorList, i, j, S, A, R, l, lr)
  return weight
