yankee_greats = {
    2: 'Derek Jeter',
    3: 'Babe Ruth',
    7: 'Mickey Mantle',
    42: 'Mariano Rivera'
}

number = int(input('\nEnter a number:\n'))

try:
    player = yankee_greats[number]
    print('\nThe player who wore', number, 'was', player)
except:
    print('\nThe number', number, 'was not worn by any yankee greats...')
# Finally statement will run no matter if the try worked or not
finally:
    print('\nList of Yankee Greats:')
    for player in yankee_greats:
        print(player, yankee_greats[player])

print('--------------------------------THE END-----------------------------\n\n')