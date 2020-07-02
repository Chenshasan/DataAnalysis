import json

score = json.loads(open('../数据提取和处理/averageScore.json', encoding='utf-8').read())
data = json.loads(open('result.json', encoding='utf-8').read())
res = {}
max = 0

for key in data:
    user = data[key]
    weight_sum = 0
    result = 0
    for case in user:
        if user[case]['commit_num'] == 0:
            raw = 0
        else:
            raw = user[case]['score_inc'] / user[case]['commit_num']
        weight = score[case]
        weight_sum += weight
        result += raw * weight
    result /= weight_sum
    res[key] = result
    if max < result:
        max = result

for key in res:
    res[key] /= max

filename = 'result2.json'
with open(filename, 'w', encoding='utf-8') as file_obj:
    json.dump(res, file_obj, ensure_ascii=False, indent=4)
