import os
import json
import csv
import pickle

path = "C:/Users/User/PycharmProjects/Pythonpro"

def recurs_dir(name_path, level=1):
    print("Level=", level, "Content: ", os.listdir(name_path))
    with (open('save.csv', "a+", encoding='utf-8') as file1,
          open('doc.txt', "ab") as file2,
            open("json.json", "a+") as file3):
        date = csv.writer(file1)
        for i in os.listdir(name_path):
            if os.path.isdir(name_path + '/' + i):
                print('Спускаемся', name_path + '/' + i)
                date.writerow([name_path + '/' + i])
                json.dump(i, file3)
                pickle.dump(i, file2)
                recurs_dir(name_path + '/' + i, level + 1)
                print("Возвращаемся в ", name_path)

recurs_dir(path)

