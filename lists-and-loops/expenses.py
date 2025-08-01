expenses = [10.6, 78, 3.3, 22.44]

total1 = 0

# You could get the sum using a for loop
for x in expenses:
    total1 += x

print('\n\nSum of expenses: $', total1, sep = '')

# OR you could use python built in method sum()
total2 = sum(expenses)
print(total2)