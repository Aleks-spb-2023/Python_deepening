
#1 задача
path = 'C:/Users/text/file.txt'

def file_path(path):
    elem = path.split("/")
    path, format = elem[0:-1], elem[-1]
    name,  extension = format.split(".")
    return "-->".join(path), name, extension

print(file_path(path))
#2 Задача

name = ['Igor', 'Aleks', "Petr", "Nikky"]
bet = [30000, 25000, 18000, 78000]
bonus = ['10.25%', '10.50%', '23.10%', '8.5%']

dic_generate = {name:st * float(pr[0:-1])/100 for name, st, pr in zip(name,bet, bonus)}
print(dic_generate)

#3 Задача

def fib_gen(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b,a + b
print(*fib_gen(10))
