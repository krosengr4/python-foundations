number1 = input("Please enter the first number:\n")
number2 = input("Please enter the second number:\n")

operator = input("Please enter the operator ('+', '-', '*', or '/'):\n")

number1_int = int(number1)
number2_int = int(number2)

if operator == "+":
    result = int(number1) + int(number2);
elif operator == "-":
    result = int(number1) - int(number2);
elif operator == "*":
    result = int(number1) * int(number2);
elif operator == "/" and int(number2) != 0:
    result = int(number1) / int(number2);

print("The result is:", result);