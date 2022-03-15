from math import pi, sin
import sys
sys.path.append('.')

import json

from utils.Sensor import createSensor
from alg.ga import ga, getBestChild
from ga.getData import getData
from ga.initSensor import initSensor

# get initial data
path = './data/initDat/initDat.json'

f = open(path, 'r')
data = json.loads(f.read())

L = data['ROIData']['length']     # length of ROI
H = data['ROIData']['height']     # height of ROI
R = data['sensorData']['range']   # sensor sensing range
A = data['sensorData']['alpha']   # sensor sensing angle

# GA constants
MAX_GENERATION = 1000
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.05
POPULATION_SIZE = 1000

# Sensor constants
S = 200            # Number of stationary sensors
M = 50             # Number of mobile sensors
DATA_PACK = 1      # Index of data pack

# Start program
LARGEST_RANGE = 0
if(0 <= A and A <= pi / 2):
  LARGEST_RANGE = max(R, 2 * R * sin(A))
dataList = getData(DATA_PACK)
sensorList = createSensor(dataList, S, A)
sortedSensor = initSensor(sensorList)
parents = ga(sortedSensor, S, M, A, R, L, LARGEST_RANGE, MUTATION_RATE,
             MAX_GENERATION, POPULATION_SIZE, CROSSOVER_RATE)
child = getBestChild(parents)
k = child.fitness

print(k)
