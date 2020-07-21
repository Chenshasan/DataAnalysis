import json
import xlrd


def prepare_data_json2txt():
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

    # 打开excel
    wb = xlrd.open_workbook('../result.xlsx')
    # 按工作簿定位工作表
    sh = wb.sheet_by_name('Sheet1')

    # json to txt
    file = open('bp_data2.txt', mode='w')
    i=1
    min = -1.386544759
    max = 2.129893327
    for user in data1:
        file.write(str(data1[user]) + " " + str(data2[user]) + " " + str(data3[user]) + " " + str(data4[user]) + " " + str(data5[
            user]) + " " + str((sh.cell(i, 6).value - min) / (max - min)) + "\n")
        i+=1
    file.close()


def prepare_data_xls2txt():
    # 打开excel
    wb = xlrd.open_workbook('../result.xlsx')
    # 按工作簿定位工作表
    sh = wb.sheet_by_name('Sheet1')
    print(sh.nrows)  # 有效数据行数
    print(sh.ncols)  # 有效数据列数
    min = -1.386544759
    max = 2.129893327
    file = open('bp_data.txt', mode='w')
    for i in range(1, sh.nrows):
        file.write(str(sh.cell(i, 1).value) + " " + str(sh.cell(i, 2).value) + " " + str(sh.cell(i, 3).value) + " " +
                   str(sh.cell(i, 4).value) + " " + str(sh.cell(i, 5).value) + " " + str((sh.cell(i, 6).value - min) / (max - min)) + "\n")
    file.close()


if __name__ == '__main__':
    prepare_data_json2txt()
