#__author:gzc
#date:2019/1/2

import json

dic = dict(name='郭志超', age=26, hobby='足球')

data = json.dumps(dic)

f = open('JSON_text','r')
data = f.read()
dic = json.loads(data)
print(dic['name'])
f.close()
