import json

def getData(index: int) -> list:
  path = './data/sensorDat/sensorDat_' + str(index) + '.json'
  sensorList = []
  f = open(path, 'r')
  data = json.loads(f.read())
  for i in data['data']:
    sensorList.append(i)
  return sensorList

print(getData(1)[0])
