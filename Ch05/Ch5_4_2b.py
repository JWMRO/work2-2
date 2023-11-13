import json

jsonfile = "./Ch05/Example.json"
with open(jsonfile, 'r') as fp:
    data = json.load(fp)     # 讀取JSON檔案並轉換成字典
json_str = json.dumps(data)  # 將字典轉成字串  
print(type(json_str)) 
print(json_str)