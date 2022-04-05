import sys
from matplotlib.axes import Axes

sys.path.append('.')

import math
import matplotlib
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt

from utils.Sensor import createSensor, Sensor

fig, ax = plt.subplots(1)

def draw(SensorList: list[Sensor], ax: Axes, a: float, r: int) -> None:
  for i in SensorList:
    ss = Wedge((i.pos.x, i.pos.y), r, math.degrees(i.beta),
               math.degrees(i.beta + 2 * a), color="r" if i.isMobile else "g", alpha=0.5)
    ax.add_artist(ss)

def visualize(sensorList, a: float, r: int):
  ax.set_aspect('equal', 'box')
  draw(sensorList, ax, a, r)
  ax.set_ylim(0, 100)
  ax.set_xlim(0, 500)
  plt.show()
