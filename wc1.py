import requests
import json

url="http://127.0.0.1:5000/postjson"

#res=requests.post("http://127.0.0.1:5000/postjson")


#files = {'file': open("tst.json", 'rb')}
datas={
 "name":"Test",
 "ID":"2"
}

#d=json.loads(datas)
#headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
headers = {'Content-Type' : 'application/json'}
r = requests.post(url, headers=headers, data=json.dumps(datas))
print(r.status_code, r.reason)
print(r.text)