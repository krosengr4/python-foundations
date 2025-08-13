import random

# def roll_dice():
#     return random.randint(1, 6) + random.randint(1, 6);

def roll1():
    return random.randint(1,6)

def roll2():
    return random.randint(1,6)


ifContinue = True

player1 = input('\nEnter the name of player one:\n')
player2 = input('Enter the name of player two:\n')

while(ifContinue):

    player1_roll1 = roll1();
    print(player1 + 's first dice is a ', player1_roll1)
    input('Hit enter to continue')

    player1_roll2 = roll2();
    print(player1 + 's second dice is a', str(player1_roll2))
    input('Hit enter to continue')

    player2_roll1 = roll1();
    print(player2 + 's first dice is a', str(player2_roll1))
    input('Hit enter to continue')

    player2_roll2 = roll2();
    print(player2 + 's second dice is a', str(player2_roll2))
    input('Hit enter to continue')

    player1_total = player1_roll1 + player1_roll2
    player2_total = player2_roll1 + player2_roll2


    if player1_total > player2_total: 
        print(player1, 'wins!\n');
    elif player1_total < player2_total:
        print(player2, 'wins!\n');
    else:
        print('It was a tie...\n');

    play_again = input('\nWould you like to play again (y or n):\n'.lower())
    if(play_again == 'n'):
        ifContinue = False;

