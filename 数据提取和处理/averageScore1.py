import json

f = open('score.json', encoding='utf-8')

cases=[]
count=[]
score=[]
users={}

res = f.read()
data = json.loads(res)

for key in data:
    print(key["case_id"])
    print(key["score"])
    if key["case_id"] in cases:
        indexOf=cases.index(key["case_id"])
        print("index"+str(indexOf))
        score[indexOf]=(score[indexOf]*count[indexOf]+key["score"])/(count[indexOf]+1)
        count[indexOf]=count[indexOf]+1
    else:
        cases.append(key["case_id"])
        count.append(1)
        score.append(key["score"])

for i in range(0,len(cases)):
    users[cases[i]]=score[i]

json_str=json.dumps(users,indent=4)
with open("D:\数据科学大作业"+"\\"+"averageScore.json",'w') as json_file:
    json_file.write(json_str)