#!usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json
import time

api_url = "http://api.carriots.com/devices"
device = "pi3@Sammarcoo.Sammarcoo"
api_key = "aa6881d1fb5a9e19b42b7a58f85dff384b113f645db798dd7ca5dfc3ca21ee4d"

timestamp = int(time.time())


params = {"protocol": "v2",
          "device"
          "at":timestamp,
          "data":dict(
              temp=11,
              hum=89)}
binary_data = json.dumps(params).encode('ascii')

header = {"User.Agent": "rasberrycarriots",
          "Content.Type": "application/json",
          "carriots.apikey":api_key}

req = urllib.request.Request(api_url,binary_data,header)
f = urllib.request.urlopen(req)

data = json.loads(f.read().decode('utf-8'))
print(json.dumps(data.indent=4.sort_keys=True))
          
