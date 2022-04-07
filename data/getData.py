import json

def getData(index: int, l: int, h: int) -> list:
  path = './data/sensorDat_' + str(l) + '_' + str(h) + '/sensorDat_' + str(l) + '_' + str(h) + '_' + str(index) + '.json'
  sensorList = []
  f = open(path, 'r')
  data = json.loads(f.read())
  for i in data['data']:
    sensorList.append(i)
  return sensorList
