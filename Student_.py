

class Names:
    def __init__(self, param):
        self.param = param


    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        value = getattr(instance, self.param_name)
        return value

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.istitle():
            raise ValueError(f'Значение {value} должно с заглавной буквы ')
        if not value.isalpha():
            raise ValueError(f'Значение {value} не должно содержать цыфры')


import csv


class Grades:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Subjects:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: str):
        data = []
        with open('subjects.csv', 'r', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                data.append(''.join(line))

            if value not in data:
                raise ValueError(f'Значение {value} нет в списке ')

class Student:
    first_name = Names(str)
    last_name = Names(str)
    father_name = Names(str)

    grade = Grades(2, 5)
    exam = Grades(0, 100)

    def __init__(self, last_name, first_name, father_name, subject, grade, exam):
        self.last_name = last_name
        self.first_name = first_name
        self.father_name = father_name
        self.subject = subject
        self.exam = exam
        self.grade = grade

    def __repr__(self):
        return f"STudent: {self.last_name} {self.first_name} {self.father_name}"


s = Student('Ivan', 'Ivanov', 'Ivanovich', 'Math', 3, 10)

print(s)