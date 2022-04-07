import sys
sys.path.append('.')

from utils.Point import Point

class Sensor:
  def __init__(self, pos: Point, range: float, beta: float, alpha: float) -> None:
    self.pos = pos
    self.beta = beta
    self.range = range
    self.alpha = alpha

class SortedSensor(Sensor):
  def __init__(self, pos: Point, range: float, beta: float, alpha: float, index: int) -> None:
    self.pos = pos
    self.range = range
    self.beta = beta
    self.alpha = alpha
    self.index = index

def createSensor(dat: list, s: int) -> list[Sensor]:
  sensors = []
  for i in range(s):
    sensors.append(Sensor(Point(float(dat[i]['pos']['x']), float(dat[i]['pos']['y'])),
                   float(dat[i]['range']), float(dat[i]['beta']), float(dat[i]['alpha'])))
  return sensors
