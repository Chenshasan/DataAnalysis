import json
import time
import urllib.request, urllib.parse
import os
import zipfile

f = open('testdata.json', encoding='utf-8')

res = f.read()
data = json.loads(res)

users=[]
for key in data:
    cases = data[key]['cases']
    user_id = str(data[key]['user_id'])
    print(user_id)
    print(cases)

    dir_name = "D:\数据科学大作业\SampleData" + "\\" + user_id
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)

    for case in cases:
        Mycase={"case_id":case["case_id"],
                "score":case["final_score"]}
        users.append(Mycase)

json_str=json.dumps(users,indent=4)
with open("D:\数据科学大作业"+"\\"+"score.json",'w') as json_file:
    json_file.write(json_str)
