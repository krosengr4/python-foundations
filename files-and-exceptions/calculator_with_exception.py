def remainder_division(a, b):
    if b == 0:
        raise Exception('Divisor cannot be zero!!')
    
    # Remember // means that it will divide to a whole number
    result = a // b
    remainder = a % b
    print(a, 'divided by', b, 'is', result, 'with a remainder of', remainder)

num1 = int(input('\nEnter a number:\n'))
num2 = int(input('Enter another number:\n'))

remainder_division(num1, num2)