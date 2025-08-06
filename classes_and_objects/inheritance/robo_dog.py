from robot import Robot

# To define a class that inherits a parent class use "class child_name(parent_name)"
class Robo_Dog(Robot):

    def make_noise(self):
        print(self.name, 'says: Woof woof!')

    def eat(self):
        print('I like bacon!')

