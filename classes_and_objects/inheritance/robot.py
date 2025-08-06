class Robot:
    
    def __init__(self, name):
        self.name = name
        self.position = [0,0]

    def walk(self, x):
        self.position[0] += x

    