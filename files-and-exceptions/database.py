import mysql.connector
import os

try:
    mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = os.getenv('SQL_PASSWORD'),
    database = 'northwind'
)
    print('Connected to the db!')

except mysql.connector.Error as err:
    print('Error:', err)

cursor = mydb.cursor()

cursor.execute('Select * from products')
my_result = cursor.fetchall()

for x in my_result:
    print(x)