import requests, json
import sys

url = "http://127.0.0.1:9000/predict_api"
#data = json.dumps({'sl':5.84,'sw':3.0,'pl':3.75,'pw':1.1})

#data = json.dumps({[     {"wt" : 150,"label" : 1 } ]})
data = json.dumps([120,1])
print(data)
#sys.exit(0)

r = requests.post(url,data)
print(r.json())