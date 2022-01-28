import json
from iconLib import get_icon

f = open('/home/pi/eink-2in7/data/weather.json')
responseStr = f.read()
responseJson = json.loads(responseStr)
responseCurr = responseJson['current']

curID = responseCurr['weather'][0]['id']

curID = input()

print(curID)

print(get_icon(curID))
