import json
from math import pi
from random import randint, uniform

index = 6
l = 100
h = 500
minRange = 10
maxRange = 20
N = 2000

path = './data/sensorDat_' + str(l) + '_' + str(h) + '/sensorDat_' + str(l) + '_' + str(h) + '_' + str(index) + '.json'

obj = {
  'name': 'sensor_data_' + str(index),
  'data': []
}
for i in range(N):
  sensorObj = {
    'pos': {
      'x': '{:.4f}'.format(uniform(0, h)),
      'y': '{:.4f}'.format(uniform(0, l))
    },
    'range': '{:.4f}'.format(uniform(minRange, maxRange)),
    'beta': '{:.4f}'.format(uniform(0, pi * 2)),
    'alpha': '{:.4f}'.format(uniform(pi / 3, 2 * pi / 3))
  }
  obj['data'].append(sensorObj)

f = open(path, 'w')
f.write(json.dumps(obj))
print('successful')
