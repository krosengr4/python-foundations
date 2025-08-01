# You can use range() to repeat things like a loop
# range(5) would create a sequence of 5 variables starting at 0 (0, 1, 2, 3, 4)
# range(0, 7, 1) would create a sequence where 0 = start, 7 = stop, and 1 = step
# So, range(2, 9, 3) would start at 2, step by 3 to 5, step to 8, and stop at 8 (2, 5, 8)

for i in range(5):
    print(i);

print('---------------------------------')

for i in range(2, 9, 3):
    print(i);

print('---------------------------------')

expenses = []

for i in range(3):
    expenses.append(float(input('Enter an expense: ')));

total = sum(expenses)
print('You spent $', total, sep = '');
