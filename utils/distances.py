import sys
sys.path.append('.')

from numpy import inf
from math import ceil, cos, sin, sqrt, atan, acos, pi

from utils.Sensor import SortedSensor, Sensor
from utils.Point import Point

def largestRange(sensor: Sensor):
  return max(sensor.range, 2 * sensor.range * sin(sensor.alpha)) if 0 <= sensor.alpha and sensor.alpha <= pi / 2 else 2 * sensor.range

def calcPointCircle(sensor: Sensor) -> list:
  x1 = sensor.pos.x + sensor.range * cos(sensor.beta)
  y1 = sensor.pos.y + sensor.range * sin(sensor.beta)
  x2 = sensor.pos.x + sensor.range * cos(sensor.beta + 2 * sensor.alpha)
  y2 = sensor.pos.y + sensor.range * sin(sensor.beta + 2 * sensor.alpha)
  return [x1, y1, x2, y2]

def dist(u: Point, v: Point) -> float:
  return sqrt((u.x - v.x)**2 + (u.y - v.y)**2)

def getPoint(s: SortedSensor | Sensor) -> list[Point]:
  p1 = Point(s.pos.x, s.pos.y)
  pos2 = calcPointCircle(s)
  p2 = Point(pos2[0], pos2[1])
  p3 = Point(pos2[2], pos2[3])
  return [p1, p2, p3]

def checkObtuse(p1: Point, p2: Point, p3: Point) -> bool:
  d1 = dist(p1, p2)
  d2 = dist(p2, p3)
  d3 = dist(p1, p3)
  return (d1 ** 2 + d2 ** 2 - d3 ** 2) < 0 or (d2 ** 2 + d3 ** 2 - d1 ** 2) < 0

def pointToLine(p: Point, u: Point, v: Point) -> float:
  d1 = dist(u, v)
  if(d1 == 0):
    return dist(p, u)
  t = ((p.x - u.x) * (v.x - u.x) + (p.y - u.y) * (v.y - u.y)) / d1 / d1
  t = max(0, min(1, t))
  d = dist(p, Point(u.x + t * (v.x - u.x), u.y + t * (v.y - u.y)))
  if (checkObtuse(p, u, v)):
    return min(dist(p, u), dist(p, v))
  return d

"""
  set of functions to check if 2 line segments are intersect
  source: https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
"""
# Given three collinear points p, q, r, the function checks if
# point q lies on line segment 'pr'
def onSegment(p: Point, q: Point, r: Point) -> bool:
  if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
    return True
  return False

def orientation(p: Point, q: Point, r: Point) -> int:
  # to find the orientation of an ordered triplet (p,q,r)
  # function returns the following values:
  # 0 : Collinear points
  # 1 : Clockwise points
  # 2 : Counterclockwise
  # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
  # for details of below formula.
  val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
  if (val > 0):
    # Clockwise orientation
    return 1
  elif (val < 0):
    # Counterclockwise orientation
    return 2
  else:
    # Collinear orientation
    return 0

# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def checkIntersect(p1: Point, q1: Point, p2: Point, q2: Point) -> bool:
  # Find the 4 orientations required for
  # the general and special cases
  o1 = orientation(p1, q1, p2)
  o2 = orientation(p1, q1, q2)
  o3 = orientation(p2, q2, p1)
  o4 = orientation(p2, q2, q1)
  # General case
  if ((o1 != o2) and (o3 != o4)):
    return True
  # Special Cases
  # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
  if ((o1 == 0) and onSegment(p1, p2, q1)):
    return True
  # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
  if ((o2 == 0) and onSegment(p1, q2, q1)):
    return True
  # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
  if ((o3 == 0) and onSegment(p2, p1, q2)):
    return True
  # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
  if ((o4 == 0) and onSegment(p2, q1, q2)):
    return True
  # If none of the cases
  return False
"""
  end
"""
def getIntersect(p1: Point, q1: Point, p2: Point, q2: Point) -> Point:
  if(onSegment(p1, p2, q2)):
    return p1
  elif(onSegment(q1, p2, q2)):
    return q1
  elif(onSegment(q2, p1, q1)):
    return q2
  elif(onSegment(p2, p1, q1)):
    return p2
  t1 = (q2.x - q1.x) / (p1.x - q1.x + q1.x - p2.x)
  t2 = (q2.y - q1.y) / (p1.y - q1.y + q1.y - p2.y)
  return Point(t1 * p1.x + (1 - t1) * q1.x, t2 * p1.y + (1 - t2) * q1.y)

def checklineArcIntersect(p1: SortedSensor | Sensor, l1: Point, l2: Point) -> bool:
  p = getPoint(p1)[0]
  if(l1.x - l2.x == 0):
    return False
  a = (l1.y - l2.y) / (l1.x - l2.x)
  c = l1.y - a * l1.x
  b = -1
  phi = (a * p1.pos.x + b * p1.pos.y + c) / p1.range / sqrt(a * a + b * b)
  if(phi > 1 or phi < 0):
    return False
  t1 = atan(b / a) + acos(-phi)
  t2 = atan(b / a) - acos(-phi)
  if (((p.x + p1.range * cos(t1) > l1.x and p.x + p1.range * cos(t1) > l2.x) or
       (p.x + p1.range * cos(t1) < l1.x and p.x + p1.range * cos(t1) < l2.x)) and
      ((p.x + p1.range * cos(t2) > l1.x and p.x + p1.range * cos(t2) > l2.x) or
       (p.x + p1.range * cos(t2) < l1.x and p.x + p1.range * cos(t2) < l2.x))):
    return False
  if ((p1.beta <= t1 and t1 <= p1.beta + 2 * a) or (p1.beta <= t2 and t2 <= p1.beta + 2 * a)):
    return True
  return False

def checkArcIntersect(p1: SortedSensor | Sensor, p2: SortedSensor | Sensor) -> bool:
  if (dist(p1.pos, p2.pos) - p1.range - p2.range > 0):
    return False
  elif (dist(p1.pos, p2.pos) - p1.range - p2.range <= 0):
    pa = getPoint(p1)
    pb = getPoint(p2)
    if (checkIntersect(pa[1], pa[2], p1.pos, p2.pos) and checkIntersect(pb[1], pb[2], p1.pos, p2.pos)):
      return True
  return False

def checkSensorOverlap(s1: SortedSensor | Sensor, s2: SortedSensor | Sensor) -> bool:
  ps1 = getPoint(s1)
  ps2 = getPoint(s2)
  return (checkIntersect(ps1[0], ps1[1], ps2[0], ps2[1]) or
          checkIntersect(ps1[0], ps1[2], ps2[0], ps2[2]) or
          checkIntersect(ps1[0], ps1[1], ps2[0], ps2[2]) or
          checkIntersect(ps1[0], ps1[2], ps2[0], ps2[1]) or
          checklineArcIntersect(s1, ps2[0], ps2[1]) or
          checklineArcIntersect(s2, ps1[0], ps1[1]) or
          checklineArcIntersect(s1, ps2[0], ps2[2]) or
          checklineArcIntersect(s2, ps1[0], ps1[2]) or
          checkArcIntersect(s1, s2))

def calcX(s: SortedSensor | Sensor) -> list[float]:
  ps = getPoint(s)
  if (s.beta > pi / 2 and s.beta < pi):
    return [ps[0].x - s.range, ps[0].x]
  if (s.beta < 2 * pi and s.beta > (pi * 3) / 2):
    return [ps[0].x, ps[0].x + s.range]
  lst = [min(ps[0].x, ps[1].x, ps[2].x)]
  lst.append(max(ps[0].x, ps[1].x, ps[2].x))
  return lst

def weakDist(sensors: list[SortedSensor | Sensor], vi: int, vj: int, S: int, l: int) -> float:
  if (vi == 0):
    vjx = calcX(sensors[vj - 1])[0]
    if (vjx <= 0):
      return 0
    return vjx
  if (vj == 0):
    vix = calcX(sensors[vi - 1])[0]
    if (vix <= 0):
      return 0
    return vix
  if (vi == S + 1):
    vjx = calcX(sensors[vj - 1])[1]
    if (vjx >= l):
      return 0
    return l - vjx
  if (vj == S + 1):
    vix = calcX(sensors[vi - 1])[1]
    if (vix >= l):
      return 0
    return l - vix
  else:
    [x11, x12] = calcX(sensors[vi - 1])
    [x21, x22] = calcX(sensors[vj - 1])
    if (x12 < x21):
      return x21 - x12
    if (x11 > x22):
      return x11 - x22
    if ((x11 < x21 and x21 < x12) or (x11 < x22 and x22 < x12)):
      return 0
    if ((x11 < x21 and x22 < x12) or (x21 < x11 and x12 < x22)):
      return 0

def minPointDist(a1: list[Point], a2: list[Point]) -> float:
  min = dist(a1[0], a2[0])
  for i in a1:
    for j in a2:
      if(min > dist(i, j)):
        min = dist(i, j)
  return min

def arcDist(s1: SortedSensor | Sensor, s2: SortedSensor | Sensor) -> float:
  p1 = getPoint(s1)
  p2 = getPoint(s2)
  if (checkIntersect(p1[0], p2[0], p1[1], p1[2]) and checkIntersect(p1[0], p2[0], p2[1], p2[2])):
    return dist(p1[0], p2[0]) - s1.range - s2.range
  return inf

def lineArcDist(s1: SortedSensor | Sensor, s2: SortedSensor | Sensor) -> float:
  p1 = getPoint(s1)
  min = inf
  gamma1 = [s1.beta + pi / 2, s1.beta - pi / 2, s1.beta + 2 * s1.alpha + pi / 2, s1.beta + 2 * s1.alpha - pi / 2]
  for i in gamma1:
    if((s2.beta < i and i < s2.beta + 2 * s1.alpha)):
      x = s2.pos.x + s2.range * cos(i)
      y = s2.pos.y + s2.range * sin(i)
      if(checkObtuse(Point(x, y), p1[0], p1[1])):
        min = pointToLine(Point(x, y), p1[0], p1[1])
      if(checkObtuse(Point(x, y), p1[0], p1[2]) and pointToLine(Point(x, y), p1[0], p1[2]) < min):
        min = pointToLine(Point(x, y), p1[0], p1[2])
  return min

def getAngle(p: Point, q: Point) -> float:
  p1 = Point(q.x - p.x, q.y - p.y)
  p2 = Point(1, 0)
  a = acos((p1.x * p2.x + p1.y * p2.y) / (sqrt(p1.x ** 2 + p1.y ** 2) + sqrt(p2.x ** 2 + p2.y ** 2)))
  if (p1.y > 0):
    return pi * 2 - a
  return inf

def pointArcDist(p: Point, s: SortedSensor | Sensor) -> float:
  ps = getPoint(s)
  if(dist(p, ps[0]) <= s.range):
    return inf
  if(s.beta < getAngle(p, ps[0]) and getAngle(p, ps[0]) < s.beta + 2 * s.alpha):
    return dist(p, ps[0]) - s.range
  return inf

def strongDist(sensors: list[SortedSensor | Sensor], vi: int, vj: int, S: int, l: int) -> float:
  if(vi == vj):
    return 0
  if(vi == 0 or vj == 0 or vi == S + 1 or vj == S + 1):
    return weakDist(sensors, vi, vj, S, l)
  if(checkSensorOverlap(sensors[vi - 1], sensors[vj - 1])):
    return 0
  else:
    p1 = getPoint(sensors[vi - 1])
    p2 = getPoint(sensors[vj - 1])
    minDist = min(minPointDist(p1, p2),
                  arcDist(sensors[vi - 1], sensors[vj - 1]),
                  lineArcDist(sensors[vi - 1], sensors[vj - 1]),
                  lineArcDist(sensors[vj - 1], sensors[vi - 1]),
                  pointArcDist(p1[0], sensors[vj - 1]),
                  pointArcDist(p1[1], sensors[vj - 1]),
                  pointArcDist(p1[2], sensors[vj - 1]),
                  pointArcDist(p2[0], sensors[vi - 1]),
                  pointArcDist(p2[1], sensors[vi - 1]),
                  pointArcDist(p2[2], sensors[vi - 1]),
                  pointToLine(p1[0], p2[0], p2[1]),
                  pointToLine(p1[0], p2[0], p2[2]),
                  pointToLine(p1[1], p2[0], p2[1]),
                  pointToLine(p1[1], p2[0], p2[2]),
                  pointToLine(p1[2], p2[0], p2[1]),
                  pointToLine(p1[2], p2[0], p2[2]),
                  pointToLine(p2[0], p1[0], p1[1]),
                  pointToLine(p2[0], p1[0], p1[2]),
                  pointToLine(p2[1], p1[0], p1[1]),
                  pointToLine(p2[1], p1[0], p1[2]),
                  pointToLine(p2[2], p1[0], p1[1]),
                  pointToLine(p2[2], p1[0], p1[2]))
    return minDist

def minNum(sensors: list[SortedSensor | Sensor], vi: int, vj: int, s: int, l: int, lr: float) -> int:
  return ceil(strongDist(sensors, vi, vj, s, l) / lr)
