import json
import os
import sys

max=-1
min=sys.maxsize

user_dir="D:\数据科学大作业\\testTime.json"
answer_dir="D:\数据科学大作业\\testAnswerTime.json"

f1 = open(user_dir, encoding='utf-8')
res1 = f1.read()
data1 = json.loads(res1)

f2 = open(answer_dir, encoding='utf-8')
res2 = f2.read()
data2 = json.loads(res2)

times={}
for user in data1:
    print(user)
    cases=data1[user]
    n=len(cases)
    timeO=[]
    for case in cases:
        case_id=case["case_id"]
        time=case["time"]
        answerTime=data2[case_id]
        tempTimeO=time/answerTime
        print(tempTimeO)
        timeO.append(tempTimeO)
        if max<tempTimeO:
            max=tempTimeO
        if min>tempTimeO:
            min=tempTimeO
    for i in range(0,n):
        timeO[i]=5*(max-timeO[i])/(max-min)
        print(timeO[i])
    res=sum(timeO)/n
    print(res)
    times[user]=res
json_str = json.dumps(times, indent=4)
with open("D:\数据科学大作业" + "\\" + "testTimeO.json", 'w') as json_file:
    json_file.write(json_str)