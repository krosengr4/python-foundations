from robot import Robot

class Robo_Cat(Robot):

    def make_noise(self):
        print(self.name, 'says: Meow Meow!')

    def eat(self):
        print('I like fish!')