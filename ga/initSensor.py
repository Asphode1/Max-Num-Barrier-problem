import sys
sys.path.append('.')

from utils.Sensor import Sensor, SortedSensor

def initSensor(sensors: list[Sensor]) -> list[SortedSensor]:
  lst = sorted(sensors, key=lambda s: s.pos.x)
  output = []
  for i in range(len(lst)):
    output.append(SortedSensor(lst[i].pos, lst[i].range, lst[i].beta, lst[i].alpha, i + 1))
  return output
