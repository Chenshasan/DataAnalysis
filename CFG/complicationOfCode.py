import json
import os
import subprocess
import time


root_dir="D:\数据科学大作业\TestData"
os.chdir(root_dir)
users={}
_users=os.listdir(root_dir)
for user in _users:
    user_id=str(user)
    dir=root_dir+"\\"+user
    cases=[]
    os.chdir(dir)
    _cases=os.listdir(dir)
    print(user_id)
    for _case in _cases:
        sdir=dir+"\\"+_case
        os.chdir(sdir)
        _uploads=os.listdir(sdir)
        print(_case)
        for _upload in _uploads:
            tdir=sdir+"\\"+_upload
            file_name=tdir+"\\"+"main.py"
            test_name=tdir+"\\"+".mooctest"+"\\"+"testCases.json"
            f = open(test_name, encoding='utf-8')
            res = f.read()
            test_data = json.loads(res)
            runTime=0
            try:
                for data in test_data:
                    ins=data["input"]
                    start = time.time()
                    p=subprocess.Popen(["python",file_name],stdin=subprocess.PIPE)
                    p.stdin.write(ins.encode('utf-8'))
                    p.communicate()
                    end = time.time()
                    runTime+=end-start
                    p.kill()
                print (runTime)
                case={"case_id":_case}
                case["time"]=runTime
                cases.append(case)
            except BrokenPipeError:
                print("未知错误")
    if len(cases)!=0:
        users[user_id]=cases
json_str=json.dumps(users,indent=4)
with open("D:\数据科学大作业"+"\\"+"testTime.json",'w') as json_file:
    json_file.write(json_str)
