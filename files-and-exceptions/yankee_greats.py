def find_yankee():
    user_search = input('\nEnter the number of the Yankee to search:\n')

    found = False
    with open('files-and-exceptions/yankee_greats.txt') as file:
        for line in file:
            if user_search in line:
                print(line)
                found = True
                break
    
    if not found:
        print("There is no Yankee with that number...")

def add_yankee():
    number = input("\nWhat is the number of the Yankee:\n")
    fname = input("What is the first name of the Yankee:\n").capitalize()
    lname = input('What is the last name of the yankee:\n').capitalize()

    with open('files-and-exceptions/yankee_greats.txt', 'a') as file:
        file.write('\n' + number + ' - ' + fname + ' ' + lname)

    print('The Yankee was added!')
    
def main():
    user_choice = input("\nWould you like to search(S) or add(A) a Yankee:\n").upper()

    if user_choice == 'S':
        find_yankee()
    elif user_choice == 'A':
        add_yankee()
    else:
        print('Please input either S or A!!!')

main()