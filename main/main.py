from math import pi, sin
import sys
sys.path.append('.')

import json
from datetime import datetime

from utils.Sensor import createSensor
from greedy.createGraph import createWeight
from greedy.Graph import WBG
from alg.ga import ga, getBestChild
from alg.greedy import greedy
from ga.getData import getData
from ga.initSensor import initSensor

# get initial data
path = './data/initDat/initDat.json'
f = open(path, 'r')
data = json.loads(f.read())

L = int(data['ROIData']['length'])       # length of ROI, default: 500
H = int(data['ROIData']['height'])       # height of ROI, default: 100
R = int(data['sensorData']['range'])     # sensor sensing range, default: 20
A = float(data['sensorData']['alpha'])   # sensor sensing angle, default: pi/4 = 0.7854

# Sensor constants
S = 200            # Number of stationary sensors, default: 200, maximum: 300
M = 50             # Number of mobile sensors, default: 50, maximum: 100
DATA_PACK = 1      # Index of data pack, from 1 to 10.

# GA constants
MAX_GENERATION = 1000     # Default: 1000
CROSSOVER_RATE = 0.8      # Default: 0.8
MUTATION_RATE = 0.05      # Default: 0.05
POPULATION_SIZE = 1000    # Default: 1000
DELTA = L / S * 10        # Default: 25

# Start program
LARGEST_RANGE = 0
if(0 <= A and A <= pi / 2):
  LARGEST_RANGE = max(R, 2 * R * sin(A))
else:
  LARGEST_RANGE = 2 * R

def startGA():
  dataList = getData(DATA_PACK)
  sensorList = createSensor(dataList, S, A)
  sortedSensor = initSensor(sensorList)
  parents = ga(sortedSensor, S, M, A, R, L, LARGEST_RANGE, MUTATION_RATE,
               MAX_GENERATION, POPULATION_SIZE, CROSSOVER_RATE)
  child = getBestChild(parents)
  k = child.fitness

  now = datetime.now()
  nowshort = now.strftime('%d%m%y-%H%M%S')
  nowLong = now.strftime('%d - %m - %Y %H:%M:%S')
  savePath = './saves/' + nowshort + '.json'

  obj = {
      'name': 'Saved data at ' + nowLong,
      'method: Genetic Algorithm'
      'population': [vars(i) for i in parents],
      'best child': vars(child),
      'max barrier': k
  }
  f = open(savePath, 'x')
  f.write(json.dumps(obj))
  f.close()
  print(k)

def startGreedy():
  dataList = getData(DATA_PACK)
  sensorList = createSensor(dataList, S, A)
  weight = createWeight(sensorList, S, A, R, L, LARGEST_RANGE)
  sensorGraph = WBG(S + 2, weight)
  k = greedy(sensorGraph, S, M, L, LARGEST_RANGE)
  print(k)

startGreedy()