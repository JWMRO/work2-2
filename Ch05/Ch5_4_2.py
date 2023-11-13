import json

data = {
   "name": "Joe Chen", 
   "score": 95, 
   "tel": "0933123456"         
}

json_str = json.dumps(data)  #將字典轉成字串
print(type(json_str))
print(json_str)
data2 = json.loads(json_str) #將字串轉成字典
print(type(data2))
print(data2)