import sys
sys.path.append('.')

from utils.Point import Point

class Sensor:
  pos = Point(0, 0)
  beta = 0
  isMobile = False

  def __init__(self, pos: Point, beta: float, isMobile: bool) -> None:
    self.pos = pos
    self.beta = beta
    self.isMobile = isMobile

class SortedSensor(Sensor):
  index = 0

  def __init__(self, pos: Point, beta: float, index: int) -> None:
    self.pos = pos
    self.beta = beta
    self.index = index
    self.isMobile = False

def createSensor(dat: list, s: int, a: float) -> list[Sensor]:
  sensors = []
  for i in range(s):
    sensors.append(Sensor(Point(dat[i]['pos']['x'], dat[i]['pos']['y']), dat[i]['beta'], a, False))
  return sensors
