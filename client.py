import requests

base_url = "https://api.weibo.com"
endpoint = "/2/statuses/public_timeline.json"
appkey = "1721783758"
access_token = "2.00hjNpRGmb7WsB0955596a4fPzvQqB"

payload = {'appkey': appkey, 'access_token' : access_token}
r = requests.get(base_url + endpoint, params=payload, timeout=1)

json_out = r.json()
print(r.url)
print(r.cookies)
#print(json_out)
