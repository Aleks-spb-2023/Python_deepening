from random import randint

import numpy as np

class Matrix:

    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise ValueError("Объект принимает матрицу")
        if not isinstance(matrix[0], list):
            raise ValueError('Элементом списка должен быть тоже список')
        self.__matrix = matrix
        self.__size = len(matrix)

    def get_matrix(self):
        return self.__matrix

    def __str__(self):
        string = ""
        for row in self.__matrix:
            string += ' '.join(map(str, row)) + "\n"
        return string

    def __eq__(self, other):
        self.__is_matrix(other)
        if self.__size != other.__size:
            return False
        res = all(len(row1) == len(row2) for row1, row2 in zip(self.__matrix, other.__matrix))
        if not res:
            return False

        return  self.__check_element(other)



    def __add__(self, other):
        self.__is_matrix(other)

        if self.__size != other.__size:
            raise ValueError("Складывать можно матрицы одной длины")
        res = all(len(row1) == len(row2) for row1, row2 in zip(self.__matrix, other.__matrix))
        if not res:
            raise ValueError("Складывать можно матрицы столбцами одинаковой длины")
        new_ls = []
        for row, row2 in zip(self.__matrix, other.__matrix):
            ls = []
            for el1, el2 in zip(row, row2):
                ls.append(el1 + el2)
            new_ls.append(ls)
        return Matrix(new_ls)


    def __mul__(self, other):
        self.__is_matrix(other)
        if self.__size != other.__size:
            raise ValueError("Умножать можно матрицы одной длины")
        res = all(len(row1) == len(row2) for row1, row2 in zip(self.__matrix, other.__matrix))
        if not res:
            raise ValueError("Умножать можно матрицы столбцами одинаковой длины")

        new = np.dot(self.__matrix, other.__matrix)
        new = map(list, new)

        return Matrix(list(new))


    def __check_element(self, obj):
        for row, row2 in zip(self.__matrix, obj.__matrix):
            for el1, el2 in zip(row, row2):
                if el1 != el2:
                    return False
        return True


    def __is_matrix(self, obj):
        '''Проверка на соответствие классу'''
        if not isinstance(obj, Matrix):
            raise ValueError("Объект должене принадлежать к классу матрица")





a = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
b = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]


m = Matrix(a)
m2 = Matrix(b)

print(m)
print(m == m2)

print(m * m2)
