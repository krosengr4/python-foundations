current_movies = {
    'The Grinch': '11:00am',
    'Rudolph': '1:00pm',
    'The Sandlot': '3:30pm',
    'Die Hard': '6:00pm'
}

print('\nWe are showing the following movies:')
print('---------------------------------------')
for key in current_movies:
    print(key);

movie = input('\nWhat movie would you like the showtime for?\n');

showtime = current_movies.get(movie);

if showtime == None:
    print('This movie is not playing!\n');
else:
    print('This movie will start at', showtime, '\n');
