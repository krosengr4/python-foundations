import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6);


ifContinue = True

while(ifContinue):
    player1 = input('\nEnter the name of player one:\n')
    player2 = input('Enter the name of player two:\n')

    roll1 = roll_dice();
    roll2 = roll_dice();

    print('\n' + player1, 'rolled:', roll1)
    print(player2, 'rolled:', roll2)

    if roll1 > roll2: 
        print(player1, 'wins!\n');
    elif roll1 < roll2:
        print(player2, 'wins!\n');
    else:
        print('It was a tie...\n');

    play_again = input('\nWould you like to play again (y or n):\n'.lower())
    if(play_again == 'n'):
        ifContinue = False;

