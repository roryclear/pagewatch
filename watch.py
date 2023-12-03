import http.client, urllib
import requests
import time
import random
import sys

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

      texts = pages[url]
      for t in texts:
        if t in res:
          sendNotif(url + " -> " + t)
          exit()      
    print(i)
    time.sleep(25)

args = sys.argv
print("args =",args)
if len(args) < 5:
  print("expected 4 arguments",len(args))
  exit()

url = args[1]
text = args[2]
user = args[3]
token = args[4]

pages = {}

pages[url] = [text]

watchPages(pages)