file_path = 'files-and-exceptions/yankee_greats.txt'

def find_yankee():
    user_search = input('\nEnter the number of the Yankee to search:\n')

    try:
        found = False
        with open(file_path) as file:
            for line in file:
                if user_search in line:
                    print(line)
                    found = True
                    break
        
        if not found:
            print("There is no Yankee with that number...")
    except FileNotFoundError as e:
        print("The file was not found...")

def add_yankee():
    number = input("\nWhat is the number of the Yankee:\n")
    fname = input("What is the first name of the Yankee:\n").capitalize()
    lname = input('What is the last name of the yankee:\n').capitalize()

    try: 
        with open(file_path, 'a') as file:
            file.write('\n' + number + ' - ' + fname + ' ' + lname)

        print('The Yankee was added!')
    except FileNotFoundError as e:
        print("The file was not found...")
    
def main():
    user_choice = input("\nWould you like to search(S) or add(A) a Yankee:\n").upper()

    if user_choice == 'S':
        find_yankee()
    elif user_choice == 'A':
        add_yankee()
    else:
        print('Please input either S or A!!!')

main()