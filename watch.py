import http.client, urllib
import requests
import time
import random

token = ""
user = ""

def sendNotif(text):
  conn = http.client.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
      "token": token,
      "user": user,
      "message": text,
      "priority": "1"
    }), { "Content-type": "application/x-www-form-urlencoded" })
  res = conn.getresponse()
  print(type(res))
  data = res.read()
  print(data)
 

def watchPages(pages):
  for i in range(1440):
    res = None
    for url in pages:
      time.sleep(random.uniform(0,10))
      try:
        res = requests.get(url).text
      except requests.exceptions.RequestException as e:
        print("req failed")
        time.sleep(10)
        continue

      print("FFS")
      texts = pages[url]
      for t in texts:
        if t in res:
          sendNotif(url + " -> " + t)
          exit()      
    print(i)
    time.sleep(25)

pages = {}

pages["https://www.websiteA.com"] = \
["somehtml","sometextorsomething"]

pages["https://www.websiteB.com"] = \
["somehtml","sometextorsomething"]

watchPages(pages)