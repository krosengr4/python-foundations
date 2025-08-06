from robo_dog import Robo_Dog
from robo_cat import Robo_Cat

print('\n-----------------------START------------------------------')

my_robo_dog = Robo_Dog('Bud')
my_robo_dog.walk(5)

my_robo_dog.make_noise()
my_robo_dog.print_location()

my_robo_cat = Robo_Cat('Bambu')
my_robo_cat.make_noise()

print("\nWhat does the cat like to eat?")
my_robo_cat.eat()

print("\nWhat does the dog like to eat?")
my_robo_dog.eat()



print('\n-----------------------THE END------------------------------\n')