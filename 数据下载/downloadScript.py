import json
import urllib.request,urllib.parse
import os
import zipfile
from urllib.parse import quote

f = open('sample.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

dir_name = "D:\PyProjects\dataAnalysis\dataSet"
os.mkdir(dir_name)
os.chdir(dir_name)

for key in data:
    cases = data[key]['cases']
    print(cases)

    for case in cases:
        print(case["case_id"], case["case_type"]);
        temp_dir = dir_name + "\\" + case["case_id"] + " " + case["case_type"]
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        os.chdir(temp_dir)
        upload_records = case["upload_records"]
        for code in upload_records:
            filename = urllib.parse.unquote(os.path.basename(code["code_url"]))
            print(filename)
            urllib.request.urlretrieve(code["code_url"], filename)

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

