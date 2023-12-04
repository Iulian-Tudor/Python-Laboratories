class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Mammal(Animal):
    def __init__(self, name, locomotion, food):
        super().__init__(name)
        self.locomotion = locomotion
        self.food = food

    def get_locomotion(self):
        return self.locomotion

    def get_food(self):
        return self.food

    def give_birth(self):
        print("I give birth to live young!")

        
class Bird(Animal):
    def __init__(self, name, locomotion, food):
        super().__init__(name)
        self.locomotion = locomotion
        self.food = food

    def get_locomotion(self):
        return self.locomotion

    def get_food(self):
        return self.food

    def lay_eggs(self):
        print("I lay eggs!")

    def fly(self):
        print("I can fly!")


class Fish(Animal):
    def __init__(self, name, water_type, food):
        super().__init__(name)
        self.water_type = water_type
        self.food = food

    def get_water_type(self):
        return self.water_type

    def get_food(self):
        return self.food

    def lay_eggs(self):
        print("I lay eggs!")

    def swim(self):
        print("I can swim!")


def main():
    mammal = Mammal("Cat", "Walks on 4 legs", "Omnivore")
    print(mammal.get_name())
    print(mammal.get_locomotion())
    print(mammal.get_food())
    mammal.give_birth()

    bird = Bird("Eagle", "flight", "Carnivore")
    print(bird.get_name())
    print(bird.get_locomotion())
    print(bird.get_food())
    bird.lay_eggs()
    bird.fly()

    fish = Fish("Shark", "swimming", "Carnivore")
    print(fish.get_name())
    print(fish.get_water_type())
    print(fish.get_food())
    fish.lay_eggs()
    fish.swim()


main()