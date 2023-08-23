import logging







logging.basicConfig(filename='logginng.log', encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s, %(levelname)s, %(message)s')



def triangrle(a, b, c):
    if not (a <= b + c) or not (b <= a + c) or not (c <= b + a):
        logging.error('Произошла ошибка')
        raise ValueError

    tr = "Равнобедренный треугольник"
    if a == b == c:
        tr = "Равносторонний треугольник"
    elif a != b and b!= c and a!= c:
        tr = "Разносторонний треугольник"
    logging.info('Программа работает в штатном режиме')
    return tr







def prime_number(number):

    D_min = 2
    D_max = 10000
    if number not in range(D_min, D_max + 1):
        logging.info('ошибка в программе ____')
        raise ValueError("число не входит в диапазон")
    count = 0
    for i in range(1, number):
        if number % i == 0:
            count += 1
    if count > 1:
        logging.info('Работает штатно!!!')
        return "Число составное"
    logging.info('Работает штатно!!!')
    return 'Число простое'


if __name__ == '__main__':
    triangrle(1, 2, 3)
    prime_number(-10)



