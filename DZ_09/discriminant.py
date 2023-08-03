import csv
import math
from random import  randint
import json


def csv_writer(file_name):
    total_str = randint(100, 10000)
    with open(file_name, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        for _ in range(total_str):
            a, b, c = randint(1, 100), randint(100, 500), randint(50, 99)
            writer.writerow([a, b, c])

# csv_writer('test.csv')

#Декоратор
def decor_discr(func):
    def wrapper(*args):
        with open('test.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = row
                result = func(int(a), int(b), int(c))
                print(result)
    return wrapper


def json_decor(func):
    def wrapper(*args, **kwargs):
        with open('js.json', 'a', encoding='utf-8') as file:
            my_dict = {}
            result = func(*args)
            my_dict[1] = result
            json.dump(my_dict, file, ensure_ascii=False, indent=2)
    return wrapper


#
# @decor_discr
# def quadro(a, b, c):
#     dis = b * b - 4 * a * c
#     sqrt_val = math.sqrt(abs(dis))
#     if dis > 0:
#        return (-b + sqrt_val ) /(2 * a), (-b - sqrt_val ) /2 * a
#
#     elif dis == 0:
#       return -b / (2 * a)
#
#     else:
#         return 'Нет корней'

@json_decor
def quadro(a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
       return (-b + sqrt_val ) /(2 * a), (-b - sqrt_val ) /2 * a

    elif dis == 0:
      return -b / (2 * a)

    else:
        return 'Нет корней'

quadro(1, 20, 1)
quadro(4, 20, 1)