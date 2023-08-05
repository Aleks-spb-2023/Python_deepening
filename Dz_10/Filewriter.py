

import csv


class FileWriter:
    def __init__(self, file_name, format="csv"):
        self.__file_name = file_name
        self.__formar = format

    def createfile(self, data):
        with open(f"{self.__file_name}.{self.__formar}", "w", encoding="utf- 8", newline="") as file:
            writer = csv.writer(file)
            for i in data:
                writer.writerow(i)



f = FileWriter('test')

data = [['1', '2', '3'], ['one', 'two', 'fre']]

f.createfile(data)