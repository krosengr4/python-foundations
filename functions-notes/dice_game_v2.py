import random

def roll_dice():
    return random.randint(1,6) + random.randint(1,6);

team1 = input('\nEnter the first team:\n')
team2 = input('Enter the second team:\n')

ifContinue = True;
team1_total = 0
team2_total = 0

while(ifContinue):
    team1_score = roll_dice();
    team2_score = roll_dice();

    print('\nThe score of the game was:')
    print(team1, team1_score)
    print(team2, team2_score)

    if team1_score > team2_score:
        print('\n' + team1, 'wins!')
        team1_total += 1
    elif team1_score < team2_score:
        print('\n' + team2, 'wins!')
        team2_total += 1
    else:
        print('It was a tie!')
    
    user_continue = input('Would you like to play again? (y or n):\n').lower()
    if(user_continue == 'n'):
        ifContinue = False;

print('----------------------------------------------------------------------')
if team1_total > team2_total:
    print('\n' + team1, 'wins overall!!!\n');
elif team1_total < team2_total:
    print('\n' + team2, 'wins overall!!!\n');
else:
    print('Nobody wins... it was a tie.\n');

print('\nFinal score:')
print(team1 + ':', team1_total)
print(team2 + ':', team2_total)
