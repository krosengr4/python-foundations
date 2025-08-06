
def search_acronym(acronym):
    print('')

    found = False

    with open('files-and-exceptions/acronyms.txt') as file:
        for line in file:
            if acronym in line:
                print(line)
                found = True
                break

    if not found:
        print("The acronym does not exists in our files...\n")

if_continue = True

while(if_continue):
    user_search = input('\nEnter an acronym to look up:\n').upper()
    search_acronym(user_search)

    user_cont = input('Would you like to continue? (y or n):\n').upper()
    if user_cont == 'N':
        print('Have a good day!\n')
        if_continue = False