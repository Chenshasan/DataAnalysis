import json
import sys

max=-1
min=sys.maxsize

dir="D:\数据科学大作业\DataAnalysis\\testTimeO.json"

f = open(dir, encoding='utf-8')
res = f.read()
data = json.loads(res)

scores={}
for user in data:
    if data[user]>max:
        max=data[user]
    if data[user]<min:
        min=data[user]
for user in data:
    scores[user]=(data[user]-min)/(max-min)

json_str = json.dumps(scores, indent=4)
with open("D:\数据科学大作业\DataAnalysis" + "\\" + "TestTimeOS.json", 'w') as json_file:
    json_file.write(json_str)