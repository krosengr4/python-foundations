import random;

print('\n\nGUESS WHAT THE COMPUTER ROLLED!\nA COMPUTER WILL RANDOMLY ROLL A SIX SIDED DICE.\nYOUR JOB IS TO GUESS WHAT IT ROLLED!')

roll = random.randint(1, 6);

user_guess = int(input('\nWhat is your guess?\n'))

if user_guess > 6 or user_guess < 1:
    print('Your guess must be between 1 and 6!!!')
else: 
    print('\nYou guessed', str(user_guess) + ". The computer rolled a", str(roll) + ".");
    print('_________________________________________________')
    if user_guess == roll:
        print('\tYOU WIN!!!\n\n')
    else:
        print('\tBoo Hoo. You lost :(\n\n')