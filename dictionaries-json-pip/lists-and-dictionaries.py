# Say you have 3 lists (breakfast, lunch, dinner). How can we combine them all into 1 list?
# In python you can have a container of containers, or a list of lists.
breakfast = ['eggs and bacon', 'pancakes', 'coffee']
lunch = ['BLT', 'PB and J', 'Turkey sandwich']
dinner = ['chicken alfredo', 'soup', 'tacos']

# List of lists
menus = [breakfast, lunch, dinner]
print('\n', menus, '\n');

# What if we want to get an item from one of these lists? (ex: Coffee)
# Our list of lists can have 2 indexes!
print(menus[0][2], '\n');

# We could also put these lists into a dictionary
dictionary_menus = {
    'breakfast': breakfast,
    'lunch': lunch,
    'dinner': dinner
}

# To print out this dictionary, we need 2 variables for key and value
for name, menu in dictionary_menus.items():
    print(name, ':', menu, '\n');


# We can also use dictionaries as objects
person = {
    'name': 'Kevin',
    'state': 'Texas',
    'age': '25'
}

# Can use the .get() method to get value for each field.
print('His name is', person.get('name'))
print('He lives in', person.get('state'))
print('He is', person.get('age'), 'years old.\n');