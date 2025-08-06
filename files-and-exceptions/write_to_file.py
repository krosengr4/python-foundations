# Ask user what acronym to add
# Open the file
# Write the new acronym and definition to file

acronym = input('\nWhat acronym would youl like to add:\n').upper()
definition = input('\nWhat is the definition for the acronym:\n').capitalize()

with open('files-and-exceptions/acronyms.txt', 'a') as file:
    file.write('\n' + acronym + ' - ' + definition)