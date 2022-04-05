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

def createStatinarySensor(dat: list, s: int) -> list[Sensor]:
  sensors = []
  for i in range(s):
    sensors.append(Sensor(Point(dat[i]['pos']['x'], dat[i]['pos']['y']), dat[i]['beta'], False))
  return sensors

def createSensor(dat: list, s: int, m: int) -> list[Sensor]:
  sensors = []
  for i in range(s):
    sensors.append(Sensor(Point(dat[i]['pos']['x'], dat[i]['pos']['y']), dat[i]['beta'], False))
  for i in range(m):
    sensors.append(Sensor(Point(dat[i]['pos']['x'], dat[i]['pos']['y']), dat[i]['beta'], True))
  return sensors
