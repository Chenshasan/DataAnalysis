import json

f = open('complication.json', encoding='utf-8')
res = f.read()
file1 = json.loads(res)

l = open('complication1.json', encoding='utf-8')
res1 = l.read()
file2 = json.loads(res1)

resList = [[] for i in range(len(file1))]

for key in file2:
    if not key in file1:
        print(key)
