import json


def prepare_data():
    # load data
    file_dir1 = "../TestTimeOS.json"
    f1 = open(file_dir1, encoding='utf-8')
    res1 = f1.read()
    data1 = json.loads(res1)

    file_dir2 = "../提交次数&分数差/answer_num.json"
    f2 = open(file_dir2, encoding='utf-8')
    res2 = f2.read()
    data2 = json.loads(res2)

    file_dir3 = "../数据提取和处理/answer_score.json"
    f3 = open(file_dir3, encoding='utf-8')
    res3 = f3.read()
    data3 = json.loads(res3)

    file_dir4 = "../数据提取和处理/complicationRes1.json"
    f4 = open(file_dir4, encoding='utf-8')
    res4 = f4.read()
    data4 = json.loads(res4)

    file_dir5 = "../提交次数&分数差/result2.json"
    f5 = open(file_dir5, encoding='utf-8')
    res5 = f5.read()
    data5 = json.loads(res5)

    # json to txt
    file = open('bp_data.txt', mode='w')
    for user in data1:
        file.write(data1[user] + " " + data2[user] + " " + data3[user] + " " + data4[user] + " " + data5[
            user] + " " + "此处填入因子分析结果" + "\n")
    file.close()


if __name__ == '__main__':
    # problem: TestTimeOS，complicationRes1 数据不全
    prepare_data()
