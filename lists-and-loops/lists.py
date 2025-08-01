empty_list = []
numbers_list = [1, 2, 3, 4]
names_list = ['mike', 'steve', 'rachel']
things_list = ['pizza', 7, 'Crazy Train', 14]

lists_list = [empty_list, numbers_list, names_list, things_list]

print('\nEmpty List:', empty_list)
print('Numbers:', numbers_list)
print('Names:', names_list)
print('Things:', things_list)
print('Lists:', lists_list, '\n')

acronyms = ['LOL', 'TTYL', 'OMG']

word = input('Enter an acronym: ').upper()

if word in acronyms:
    print(word, 'is already in the list!')
else:
    print(word, 'is not in the list yet! Let me add it!')
    acronyms.append(word)

print(acronyms, '\n')
