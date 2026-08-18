class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.hunger = 50

    def meow(self):
        print('Мяу')

    def feed(self, amount):
        if self.hunger-amount > 0:
            self.hunger -= amount
        else:
            self.hunger = 0

    def is_hunger(self):
        if self.hunger > 20:
            return True
        else:
            return False

    species = 'кот'

    @classmethod
    def get_species(cls):
        return cls.species


tom = Cat('tom', 'red')
print(tom.hunger)
tom.feed(10)
print(tom.hunger)
tom.feed(40)
print(tom.hunger)
tom.feed(1)
print(tom.hunger)

print(tom.get_species())
