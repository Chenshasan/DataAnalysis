import json

f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

res = {}
max_commit_num = 0
min_commit_num = 1000
max_score_inc = 0
min_score_inc = 100
# res的结构：
# res是一个字典，key为user_id，value为以case_id为索引的对象case，对象case包含case_type, valid_time, commit_num, score_inc

for key in data:  # data其实是一个字典，key是这个字典的键
    user_id = data[key]['user_id']
    cases = data[key]['cases']
    res[user_id] = {}
    for case in cases:
        case_id = case['case_id']
        final_score = case['final_score']
        upload_records = case['upload_records']
        res[user_id][case_id] = {}
        res[user_id][case_id]['case_type'] = case['case_type']
        res[user_id][case_id]['commit_num'] = len(upload_records)
        # begin_score = 0
        # for record in upload_records:  # 从第一次非零分提交开始
        #    if record['score'] != 0:
        #        begin_score = record['score']
        if len(upload_records) == 0:
            res[user_id][case_id]['commit_num'] = 152  # 这是跑出来的最大结果
            res[user_id][case_id]['score_inc'] = 0
        elif upload_records[0]['score'] == 100:  # 如果一开始提交就是满分，认为其debug水平为100
            res[user_id][case_id]['score_inc'] = 100
        else:
            res[user_id][case_id]['score_inc'] = final_score - upload_records[0]['score']
            if res[user_id][case_id]['score_inc'] < 0:
                res[user_id][case_id]['score_inc'] = 0
        # res[user_id][case_id]['valid_debug_time'] = 0
        # for i in range(1, len(upload_records)):
        #     inc_time = upload_records[i]['upload_time'] - upload_records[i - 1]['upload_time']
        #     if inc_time > 12 * 3600:
        #         res[user_id][case_id]['valid_debug_time'] += inc_time - 12 * 3600
        #     else:
        #         res[user_id][case_id]['valid_debug_time'] += inc_time
        if res[user_id][case_id]['commit_num'] > max_commit_num:
            max_commit_num = res[user_id][case_id]['commit_num']
        if res[user_id][case_id]['commit_num'] < min_commit_num:
            min_commit_num = res[user_id][case_id]['commit_num']
        if res[user_id][case_id]['score_inc'] > max_score_inc:
            max_score_inc = res[user_id][case_id]['score_inc']
        if res[user_id][case_id]['score_inc'] < min_score_inc:
            min_score_inc = res[user_id][case_id]['score_inc']
for user in res:
    for case in res[user]:
        res[user][case]['commit_num'] = (res[user][case]['commit_num'] - min_commit_num) / (max_commit_num - min_commit_num)
        res[user][case]['score_inc'] = (res[user][case]['score_inc'] - min_score_inc) / (max_score_inc - min_score_inc)
filename = 'result.json'
with open(filename, 'w', encoding='utf-8') as file_obj:
    json.dump(res, file_obj, ensure_ascii=False, indent=4)
