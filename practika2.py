class Animal:
    def __init__(self, name, species):
        self.name = name
        self._species = species
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not isinstance(age, int):
            print('Возраст должен быть целым числом')
        elif age > 0:
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


tom = Cat('Tom', 'brown')
chop = Dog('Chop', 'buld')

tom.voice()
tom.purr()

tom.get_age()
tom.set_age(6)
tom.get_age()
tom.set_age(-7)
tom.set_age(None)
