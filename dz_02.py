from fractions import Fraction
from math import *
def convers_number(num):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                        13: 'D', 14: 'E', 15: 'F'}

    hexadecimal = ''
    while num > 0:
        rem = num % 16
        hexadecimal = conversion_table[rem] + hexadecimal
        num  = num // 16
    return hexadecimal


def sum_deciminal(dr1, dr2):
    drob1 = Fraction(dr1)
    drob2 = Fraction(dr2)
    pr = drob1 * drob2
    sm = drob1 + drob2
    return float(pr), float(sm)





