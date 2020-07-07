import pandas as pd
import xlwt
import numpy as np
import json
import os
from math import sqrt

file_dir1 = "D:\数据科学大作业\DataAnalysis\DataAnalysis\TestTimeOS.json"
f1 = open(file_dir1, encoding='utf-8')
res1 = f1.read()
data1 = json.loads(res1)

file_dir2="D:\数据科学大作业\DataAnalysis\DataAnalysis\提交次数&分数差\\answer_num.json"
f2 = open(file_dir2, encoding='utf-8')
res2 = f2.read()
data2 = json.loads(res2)

file_dir3="D:\数据科学大作业\DataAnalysis\DataAnalysis\数据提取和处理\\answer_score.json"
f3 = open(file_dir3, encoding='utf-8')
res3 = f3.read()
data3 = json.loads(res3)

file_dir4="D:\数据科学大作业\DataAnalysis\DataAnalysis\数据提取和处理\complicationRes1.json"
f4 = open(file_dir4, encoding='utf-8')
res4 = f4.read()
data4 = json.loads(res4)

file_dir5="D:\数据科学大作业\DataAnalysis\DataAnalysis\提交次数&分数差\\result2.json"
f5 = open(file_dir5, encoding='utf-8')
res5 = f5.read()
data5 = json.loads(res5)



datas=[]

for cur_user in data1:
    user={}
    user['user_id']=cur_user
    user['timeO']=data1[cur_user]
    user['num']=data2[cur_user]
    user['averageScore']=data3[cur_user]
    user['complication']=data4[cur_user]
    user['debugInc']=data5[cur_user]
    datas.append(user)

pf=pd.DataFrame(datas)
order=['user_id','timeO','num','averageScore','complication','debugInc']
pf=pf[order]
columns_map={
    'user_id':'用户id',
    'timeO':'时间复杂度得分',
    'num':'题目数量',
    'averageScore':'平均得分',
    'complication':'代码复杂度得分',
    'debugInc':'debug效率得分'
}
pf.rename(columns=columns_map,inplace=True)
file_path=pd.ExcelWriter('userDatas.xlsx')
pf.fillna(' ',inplace=True)
pf.to_excel(file_path,encoding='utf-8',index=False)

file_path.save()