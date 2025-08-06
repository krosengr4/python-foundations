# Use with keyword to open files to make sure it closes when it is done
# read() method will read the whole file as a string
# readlines() returns a list of strings of each line in the file

print('\n-----ALL ACRONYMS-----')
with open('files-and-exceptions/acronyms.txt') as file:
    result = file.readlines()
    for line in result:
        print(line)