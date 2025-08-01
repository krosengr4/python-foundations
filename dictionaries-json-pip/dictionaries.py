# Dictionaries maps keys to values. Uses key value pairs(kvp)
# Uses curly brackets
# Order is random

# Ex: Acronym is the key and the meaning is the value
acronyms = {'LOL': 'laugh out loud', 'TTYL': 'talk to you later', 'IDK': 'I dont know'}
# Adding acronym to dictionary
acronyms['TBH'] = 'to be honest';

print('\n', acronyms, '\n');

# Updating values
acronyms['IDK'] = 'dunno';
print(acronyms['IDK'], '\n')

# Delete a value 
del acronyms['LOL'];

definition = acronyms.get('LOL')
if definition:
    print(definition, '\n');
else:
    print('Key doesnt exists!\n');

sentence = 'IDK' + 'what happened' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH');

print(translation);