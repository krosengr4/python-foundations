class Robot:

    def __init__(self, name):
        self.name = name
        self.position = [0,0]

    def walk(self, x):
        self.position[0] += x

    def eat(self):
        print("I like food")

    def print_location(self):
        print(self.name, 'location is:', self.position)

    