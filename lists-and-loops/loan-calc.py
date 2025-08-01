# Get details of loan
money_owed = float(input('\n\nHow much money, in dollars, do you owe?\n'));
apr = float(input('What is the apr of the loan?\n'));
payment = float(input('How much will you pay off each month?\n'));
months = int(input('How many months do you want to see the results for?\n'));

monthly_rate = apr/100/12;

for i in range(months):
    # Calculate interest to pay
    interest_paid = money_owed * monthly_rate

    # Add in interest
    money_owed = money_owed + interest_paid

    if(money_owed - payment < 0):
        print('\nThe last payment is', money_owed)
        print('You payed off the loan in', i + 1, 'months!\n')
        break;

    # Make payment
    money_owed = money_owed - payment;
    print('\nPaid', payment, 'of which', interest_paid, 'is in interest')
    print('Now I owe', money_owed)