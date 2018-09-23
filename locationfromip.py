from urllib.request import urlopen
import json
web = 'http://api.ipstack.com/'
ip = '134.201.250.155'
page = '?access_key=4685f1d27a16a6333dc5a992c7d7d593'

webpage = web + ip + page
f = urlopen(webpage)
json_string = f.read()
parsed_json = json.loads(json_string)
f.close()
latitude = parsed_json.get('latitude')
longitude = parsed_json.get('longitude')
print(latitude ," " , longitude)