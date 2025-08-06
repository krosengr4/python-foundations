# The keyword for functions are "def"
# def 'function name'(parameters):
# Functions need to be defined first at the top of the file before they can be called

# Create function with def keywork that prints Hello name
def greeting(name):
    print('Hello', name + '!\n');

# Get the input of the users name
name = input('\nPlease enter your name:\n')

# Call the function with the users input passed in
greeting(name);
