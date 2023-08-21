from doctest import testmod

def prime_number(number):
    """
    >>> prime_number(7)
    'Число простое'
    >>>  prime_number(6)
    "Число составное"
    """

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

testmod(verbose=True)