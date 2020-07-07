import json

f = open('complicationRes.json', encoding='utf-8')
res = f.read()
file = json.loads(res)

res={}

for key in file:
    caseList=file[key]
    print(caseList)
    count=0
    for case in caseList:
        count=count+case["ratio"]
    if len(caseList)!=0:
        res[key]=count/len(caseList)
    else:
        res[key]=1.0

json_str=json.dumps(res,indent=4)
print('aaa')
with open("D:\数据科学大作业"+"\\"+"complicationRes1.json",'w') as json_file:
    json_file.write(json_str)
