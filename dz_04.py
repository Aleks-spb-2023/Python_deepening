# 1 Задание
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

def matrix_trans(matr):
    new_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


# print(matrix_trans(matrix))

#2 Задание


def get_dict(**kwargs):
    d= {}
    for k, v in kwargs.items():
        try:
            d[v] = k
        except:
            d[str(v)] = k
    return d


# print(get_dict(a='45', g='4545', h=[1, 5, 6]))

# 3 Задача

list_operation = []
DEPOSIT = 0

def atm_():
    return DEPOSIT


def replenish_atm(money:int)-> int:
    global DEPOSIT
    global list_operation
    if money < 50:
        raise TypeError("Сумма должна быть не менее 50 рублей")
    if money % 50 != 0:
        raise TypeError("Сумма должна быть кратна 50")
    DEPOSIT += money
    list_operation.append(f'Внесено {money} р')


def take_atm(money):
    global DEPOSIT
    global list_operation
    if money > DEPOSIT:
        raise TypeError("Не достаточно средств")
    if money % 50 != 0:
        raise TypeError("Сумма должна быть кратна 50")
    DEPOSIT -= money
    list_operation.append(f"Снято {money} р")

print(atm_())
replenish_atm(500)
replenish_atm(1000)
print(list_operation)
print(atm_())
take_atm(300)
take_atm(600)
print(list_operation)
print(atm_())
















