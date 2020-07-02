import json

f = open('complication.json', encoding='utf-8')
res = f.read()
file1 = json.loads(res)

l = open('complication1.json', encoding='utf-8')
res1 = l.read()
file2 = json.loads(res1)

res={}

for key in file1:
    i=0
    j=0
    case=[]
    while i<len(file1[key]) and j<len(file2[key]):
        print(file1[key][i]["case_id"])
        print(file2[key][j]["case_id"])

        if file1[key][i]["case_id"]==file2[key][j]["case_id"]:
            result=int(file1[key][i]["complication"])/int(file2[key][j]["complication"])
            print(result)
            case.append({
                "case_id":file1[key][i]["case_id"],
                "ratio":result
            })
            i=i+1
            j=j+1
        else:
            if int(file1[key][i]["case_id"])<int(file2[key][j]["case_id"]):
                i=i+1
            else:
                j=j+1
    res[key]=case
    if key == "8318" and file1[key][i-1]["case_id"] == "2989":
        print("aaa")
        break


json_str=json.dumps(res,indent=4)
print('aaa')
with open("D:\数据科学大作业"+"\\"+"complicationRes.json",'w') as json_file:
    json_file.write(json_str)