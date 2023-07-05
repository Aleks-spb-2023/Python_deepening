from random import randint

def triangrle(a, b, c):
    if not (a <= b + c) or not (b <= a + c) or not (c <= b + a):
        raise TypeError("Треугольник не существует")

    tr = "Равнобедренный треугольник"
    if a == b == c:
        tr = "Равносторонний треугольник"
    elif a != b and b!= c and a!= c:
        tr = "Разносторонний треугольник"
    return tr


# print(triangrle(3, 1, 2))


def prime_number(number):
    D_min = 2
    D_max = 10000
    if number not in range(D_min, D_max + 1):
        raise ValueError("число не входит в диапазон")
    count = 0
    for i in range(1, number):
        if number % i == 0:
            count += 1
    if count > 1:
        return "Число составное"
    return 'Число простое'


# n = int(input('Введите число от 2 до 100000'))
# print(prime_number(n))


def random_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    RAND = randint(LOWER_LIMIT, UPPER_LIMIT)

    for i in range(10):
        num = int(input("Угадайте число от 0 до 10000"))
        if num == RAND:
            print(f'ВЫ угадали число {RAND}')
            return
        elif num > RAND:
            print('Меньше')
        else:
            print('Больше')
    print(f'Это было число {RAND}')



# random_number()