import json
import time
import urllib.request, urllib.parse
import os
import zipfile

f = open('testdata.json', encoding='utf-8')

res = f.read()
data = json.loads(res)

dir_name = "D:\PyProjects\dataAnalysis\dataSet"
os.mkdir(dir_name)
os.chdir(dir_name)

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
        if case["final_score"] != 100:
            continue;
        print(case["case_id"], case["case_type"]);
        temp_dir = dir_name + "\\" + case["case_id"] + case["case_type"]
        if os.path.exists(temp_dir):
            continue;
        os.mkdir(temp_dir)
        os.chdir(temp_dir)
        upload_records = case["upload_records"]
        isDownload = False
        for code in upload_records:
            if code["score"] == 100:
                filename = urllib.parse.unquote(os.path.basename(code["code_url"]))
                isDownload = True
        if isDownload:
            print(filename)
            urllib.request.urlretrieve(code["code_url"], filename)
            time.sleep(0.35)

        extension = ".zip"

        for item in os.listdir(temp_dir):
            os.chdir(temp_dir)
            if item.endswith(extension):
                file_name = os.path.abspath(item)
                zip_ref = zipfile.ZipFile(file_name)
                final_dir = file_name.replace(".zip", "")
                if os.path.exists(final_dir):
                    continue;
                os.mkdir(final_dir)
                zip_ref.extractall(final_dir)
                zip_ref.close()
                os.chdir(final_dir)
                for code in os.listdir(final_dir):
                    if code.endswith(extension):
                        file_Name = os.path.abspath(code)
                        zip_ref = zipfile.ZipFile(file_Name)
                        zip_ref.extractall(final_dir)
                        zip_ref.close();
                        os.remove(file_Name)
                os.remove(file_name)
