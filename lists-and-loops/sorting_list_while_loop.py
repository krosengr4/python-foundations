# Exercise 5: Sorting a List Using a While Loop (Nearly Impossible)
# 1	Use randint to generate 5 random numbers (import random). Put them in a list in the order they were generated.
# 2	Using a loop, determine the min, max, and sum of the list.
# 3 Create an empty list. Populate the empty list in order from smallest number in original list to largest. (Hint: May need loop nested in another loop)
# 4 Print out the sum, min, max and the new list sorted from lowest to highest.

import random

number1 = random.randint(1, 100);
number2 = random.randint(1, 100);
number3 = random.randint(1, 100);
number4 = random.randint(1, 100);
number5 = random.randint(1, 100);

numbers = [number1, number2, number3, number4, number5];
sorted_numbers = [];

print("\nOriginal List:", str(numbers));

sum = 0;
min = numbers[0];
max = numbers[0];

for x in numbers:
    sum += x
    if(x > max):
        max = x
    if(x < min):
        min = x

while numbers:
    smallest = numbers[0];
    for x in numbers:
        if x < smallest:
            smallest = x
    sorted_numbers.append(smallest)
    numbers.remove(smallest)

print("\nMin: ", str(min))
print("Max:", str(max))
print("Sum", str(sum))

print("\nSorted numbers list: " + str(sorted_numbers), "\n");
            