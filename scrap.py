from ebaysdk.finding import Connection as finding
from ebaysdk.exception import ConnectionError
import requests

import geopy
from geopy.geocoders import Nominatim

Keywords = input()


try:
    api = finding(appid="SHREYANS-Zoocchin-PRD-1f8f85c9b-c4909607", config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': Keywords})
    print(response.json())
    # raw_data = response.dict().get('searchResult')
    # allitems = raw_data.get('item')
    # print(allitems[0])
    # print("--")
    # pc = allitems[0].get('postalCode')
    # loc = allitems[0].get('location')
    # print(pc)
    # print(loc)

    # geolocator = Nominatim(user_agent="hello")
    # location =geolocator.geocode(loc)
    # print((location.latitude, location.longitude))

except ConnectionError as e:
    print(e)
    print(e.response.dict())
