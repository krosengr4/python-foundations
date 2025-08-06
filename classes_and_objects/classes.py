# Classes are like blueprints to create objects from
# Objects have both state(noun) and behavior(verb)
# For example lets take the object of a dog
# The state may be the name, the breed, or if it is hungry
# The behavior may be barking, running, or whagging its tail 

# To define a class use the class keyword and the class name (usually uppercase first letter)
# Then you type def __init__ to define its properties

class Robot_Dog:
    # Class properties / state
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Class behaviors
    def bark(self):
        print("Woof woof!")

my_dog = Robot_Dog('Spot', 'Dalmation')
print('Dog name:', my_dog.name)
print('Dog Breed:', my_dog.breed)

my_dog.bark()

        