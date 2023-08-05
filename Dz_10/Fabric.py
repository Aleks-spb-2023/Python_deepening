
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'Имя животного - {self.name}'

    def get_age(self):
        return f'Возраст животного = {self.age}'

    def __str__(self):
        return f'name = {self.name}, age = {self.age}'


class Fish(Animal):
    def __init__(self, fins, name, age):
        super().__init__(name, age)
        self.fins = fins

    def get_fins(self):
        return f'Уникальное свойство для рыб наличие плавников - {self.fins}'

    def __str__(self):
        return f'name = {self.name}, age = {self.age}, wings = {self.fins}'


class Birds(Animal):
    def __init__(self, wings, name, age):
        super().__init__(name, age)
        self.wings = wings

    def get_wings(self):
        return f'Уникальное свойство для птиц наличие крыльев - {self.wings}'

    def __str__(self):
        return f'name = {self.name}, age = {self.age}, wings = {self.wings}'




class Fabric:
    def __init__(self, animal_type, *parametrs):
       self.papametrs = parametrs
       self.type = animal_type

    def create_animal(self):
       return self.type(*self.papametrs)


f = Fabric(Birds, 'Крыло', 'Птица', 1000)

b = f.create_animal()

for i in b.__dict__.values():
    print(i)

