# Using library to import random guess for computer
import random;

random_num = random.randint(1, 3);

if random_num == 1:
    computer_choice = "R";
elif random_num == 2:
    computer_choice = "P";
else:
    computer_choice = "S";

user_choice = input('Do you want rock paper or scissors? (Type R, P, or S)\n').upper();

if(user_choice == computer_choice):
    print("TIE! Both chose", user_choice);
elif user_choice == "R":
    if computer_choice == "S":
        print("User wins! Rock > Scissors!");
    else: 
        print('Computer wins. Paper > Rock');
elif user_choice == "P":
    if computer_choice == "R":
        print('User Wins! Paper > Rock');
    else:
        print('Computer wins. Scissors > Paper');
elif user_choice == "S":
    if computer_choice == "P":
        print("User wins! Scissors > Paper");
    else:
        print('Computer wins: Rock over Scissors.');