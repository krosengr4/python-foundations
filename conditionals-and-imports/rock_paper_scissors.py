# Using library to import random guess for computer
import random;

def play_game(user_choice):
    random_num = random.randint(1, 3);

    if random_num == 1:
        comp_choice = 'R';
    elif random_num == 2:
        comp_choice = 'P';
    elif random_num == 3:
        comp_choice = 'S';

    print('\nUser chose:', user_choice)
    print('Computer chose:', comp_choice)

    if user_choice == comp_choice:
        print("TIE! Both chose", user_choice);
    elif user_choice == "R":
        if comp_choice == "S":
            print("User wins!")
        else: 
            print('Computer wins')
    elif user_choice == "P":
        if comp_choice == "R":
            print('User Wins!')
        else:
            print('Computer wins.');
    elif user_choice == "S":
        if comp_choice == "P":
            print("User wins!")
        else:
            print('Computer wins.');

ifContinue = True;

while ifContinue:
    user_choice = input('\nEnter rock paper or scissors (R, P, or S):\n').upper()
    play_game(user_choice)

    if_play_again = input('\nWould you like to play again? (y or n):\n')
    if if_play_again == 'n':
        print('-------------------------------------------------------')
        ifContinue = False;
    elif if_play_again != 'y':
        print('Invalid response. Shutting down.')
        ifContinue = False;

        
