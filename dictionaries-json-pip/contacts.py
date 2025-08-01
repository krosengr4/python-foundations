contacts = {
    'number_of_students': 4,
    'students': [
        {'name': 'Kevin', 'email': 'kevin@mail.com'},
        {'name': 'Sarah', 'email': 'sarah@mail.com'},
        {'name': 'Henry', 'email': 'henry@mail.com'},
        {'name': 'Rachel', 'email': 'rachel@mail.com'}
    ]
}

print('\nStudents emails:')
print('_________________________')
for student in contacts['students']:
    print(student['email']);

print('');