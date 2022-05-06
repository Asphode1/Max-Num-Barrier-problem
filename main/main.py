import sys
sys.path.append('.')

import json
from datetime import datetime
from math import pi, sin

from utils.Sensor import createSensor
from alg.ga import ga, getBestChild
from alg.greedy import greedy
from greedy.createGraph import createWeight
from greedy.Graph import WBG
from data.getData import getData
from ga.initSensor import initSensor

# get initial data

ROI_SIZE = 2  # size of ROI; 1 = small, 40 * 200; 2 = large, 100 * 500

path = './data/initData/data_' + str(ROI_SIZE) + '.json'
f = open(path, 'r')
data = json.loads(f.read())

L = int(data['ROIData']['L'])            # Length of ROI
H = int(data['ROIData']['H'])            # Height of ROI
R = int(data['sensorData']['range'])     # mobile sensor sensing range
A = float(data['sensorData']['alpha'])   # mobile sensor sensing angle
S = int(data['sSensor'])                 # Number of stationary sensors
M = int(data['mSensor'])                 # Number of mobile sensors
DATA_PACK = 1                            # Index of data pack, from 1 to 10.

# GA constants

MAX_GENERATION = 1000     # Default: 1000
CROSSOVER_RATE = 0.8      # Default: 0.8
MUTATION_RATE = 0.05      # Default: 0.05
POPULATION_SIZE = 1000    # Default: 1000
DELTA = L / S * 10        # Default: 25

# calculate Largest Range of Mobile sensor
LARGEST_RANGE = 0
if(0 <= A and A <= pi / 2):
  LARGEST_RANGE = max(R, 2 * R * sin(A))
else:
  LARGEST_RANGE = 2 * R

# start program using Genetic Algorithm
def startGA():
  dataList = getData(DATA_PACK, L, H)
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
  print('Data saved in' + savePath)
  print('k =', k)

# start program using Greedy Algorithm
def startGreedy():
  dataList = getData(DATA_PACK, L, H)
  sensorList = createSensor(dataList, S)
  weight = createWeight(sensorList, S, L, LARGEST_RANGE)
  sensorGraph = WBG(S + 2, weight)
  k = greedy(sensorGraph, S, M, L, LARGEST_RANGE)
  print('#######################################')
  print('# Data pack =', DATA_PACK)
  print('# L =', L)
  print('# H =', H)
  print('# Number of Stationary Sensor =', S)
  print('# Number of Mobile Sensor =', M)
  print('# Sensing Range =', R)
  print('# Sensing Angle =', A)
  print('# Maximum Barrier =', k)
  print('#######################################')

# main function
def start():
  print('PROGRAM TO SOLVE MAX-NUM BARRIER PROBLEM')
  print('+ Select solving method:')
  print('1. Genetic Algorithm')
  print('2. Greedy Algorithm')
  i = int(input('Method: '))
  while(i != 1 and i != 2):
    i = int(input('Wrong input, try again:'))
  match i:
    case 1:
      print('\nUsing Genetic Algorithm\n')
      startGA()
      exit()
    case 2:
      print('\nUsing Greedy Algorithm\n')
      startGreedy()

start()
