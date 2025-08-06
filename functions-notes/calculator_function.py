# Define functions with the def keyword
def addition(a, b):
    return a + b;
def subtraction(a, b):
    return a - b;
def multiplication(a, b):
    return a * b;
def division(a, b):
    if b == 0:
        print("Cannot divide by zero!!!\n")
    else:
        return a / b;

number1 = float(input('\nEnter the first number:\n'))
number2 = float(input('Enter the second number:\n'))
operation = input("Enter the operatation('+, -, *, or /)):\n")

if operation == '+':
    result = addition(number1, number2);
elif operation == '-':
    result = subtraction(number1, number2);
elif operation == '*':
    result = multiplication(number1, number2);
elif operation == '/':
    result = division(number1, number2);
else:
    print('Please enter a valid operation with no spaces!!!');

print('The result is:', result, '\n');