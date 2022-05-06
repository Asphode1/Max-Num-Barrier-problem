from math import pi
import json

n = 10
path = './data/txt/txt/W0500-H0100-N0100-M050-' + (str(0) if n != 10 else '') + str(n) + '.txt'
f = open(path, 'r')
data = f.readlines()
obj = {
  'name': 'sensor_data_' + str(n),
  'data': []
}
for i in range(1, len(data)):
  s = data[i].split()
  sensorObj = {
    'pos': {
      'x': '{:.4f}'.format(float(s[0])),
      'y': '{:.4f}'.format(float(s[1]))
    },
    'range': '{:.4f}'.format(float(s[2])),
    'beta': '{:.4f}'.format(float(s[4]) / 180 * pi),
    'alpha': '{:.4f}'.format(float(s[3]) / 180 * pi)
  }
  obj['data'].append(sensorObj)

output = './data/txt/json/W0500-H0100-N0100-M050-' + (str(0) if n != 10 else '') + str(n) + '.json'
f = open(output, 'w')
f.write(json.dumps(obj))
print('successful')
