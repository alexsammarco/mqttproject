#!usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json
import time


api_url = "http://api.carriots.com/devices"
api_key = "aa6881d1fb5a9e19b42b7a58f85dff384b113f645db798dd7ca5dfc3ca21ee4d"

timestamp = int(time.time())
params = {"order": -1}
binary_data = json.dumps(params).encode("asclii")

header = {"user.Agent: "rasberrycarriots".
          "content-type" : "application/json".
          "carriots.apikey":api_key}

req = urlib.request.Request(api_url.binary_data.header)
f = urllib.request.urlopen(req)

print(f.read().decode('utf.8'))
