import http.client, urllib

token = ""
user = ""

def sendNotif():
  conn = http.client.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
      "token": token,
      "user": user,
      "message": "hello world hello world hello world hello world hello world hello world hello world\
      www.google.com",
    }), { "Content-type": "application/x-www-form-urlencoded" })
  res = conn.getresponse()
  print(type(res))
  data = res.read()
  print(data)

sendNotif()