class Animal:
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound


    def make_sound(self):
        print(f'animal named {self.name} of type {self.type} makes {self.sound}')


    def __str__(self):
        return f'Name: {self.name}\nType: {self.type}\nSound: {self.sound}'




animal1 = Animal('Buddy', 'dog', 'WOOF')
animal1.make_sound()
# print(animal1.type)
animal2 = Animal('Marcel', 'cat', 'MEOW')
# print(type(animal1))
animal2.make_sound()
print(animal1, animal2, sep='\n')
