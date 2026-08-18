class Animal:
    def __init__(self, name, species):
        self.name = name
        self._species = species
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Ошибка неправильный возраст!')

    def voice(self):
        print('Звук')


class Cat(Animal):

    def __init__(self, name, color):
        self.color = color
        super().__init__(name, 'Кошка')

    def voice(self):
        print('Мяу!')

    def purr(self):
        print('Мур-мур...')


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name, 'Собака')

    def voice(self):
        print('Гав!')
