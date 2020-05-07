"""
The purpose of this program is to work through
the chapter 17-2 exercises in one complete script
I have added print statements and alter the SELECT
using JOIN due to errors.

Author: Jacques LaCour
Date: 05/06/2020
"""

import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.options.display.max_columns=10
print('All From Authors')
print(pd.read_sql("""SELECT *
            FROM authors""", connection, index_col=['id']))
print('\nAll From Titles')
print(pd.read_sql("""SELECT *
            FROM  titles""", connection))
df = pd.read_sql("""SELECT *
                 FROM author_ISBN""", connection)
print('\nAll from Author_ISBN Table')
print(df.head())

print('\nFirst and Last From Authors')
print(pd.read_sql("""SELECT first, last
            FROM authors""", connection))

print('\nTitle, Edition, Copyright FROM Titles')
print(pd.read_sql("""SELECT title, edition, copyright 
            FROM titles 
            WHERE copyright > '2016'""", connection))

print('\nID, First, Last From Authors with WHERE')
print(pd.read_sql("""SELECT id, first, last
            FROM  authors
            WHERE last LIKE'D%'""", connection, index_col=['id']))

print('\nID, First, Last From Authors with WHERE')
print(pd.read_sql("""SELECT id, first, last
            FROM  authors
            WHERE first LIKE'_b%'""", connection, index_col=['id']))

print('\nTitle From Titles with ORDER BY')
print(pd.read_sql("""SELECT title
            FROM titles
            ORDER BY title ASC""", connection))

print('\nID, First, Last From Authors with ORDER BY')
print(pd.read_sql("""SELECT id, first, last
            FROM  authors
            ORDER BY last, first""", connection, index_col=['id']))

print('\nID, First, Last From Authors With ORDER BY')
print(pd.read_sql("""SELECT id, first, last
            FROM  authors
            ORDER BY last DESC, first ASC""", connection, index_col=['id']))

print('\nISBN, Title, Edition, Copyright From Titles With WHERE And ORDER BY')
print(pd.read_sql("""SELECT isbn, title, edition, copyright
            FROM titles
            WHERE title LIKE '%How to Program'
            ORDER BY title""", connection))

print('\nFirst, Last, ISBN with JOIN and ORDER BY')
print(pd.read_sql("""SELECT first, last, isbn 
            FROM authors
            JOIN author_ISBN
            ON authors.id = author_ISBN.id
            ORDER BY last, first""", connection).head())

cursor=connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) 
                        VALUES ('Sue','Red')""")
print('\nID, First, Last From Authors')
print(pd.read_sql("""SELECT id, first, last
            FROM authors""", connection, index_col=['id']))

cursor = cursor.execute("""UPDATE authors 
                        SET last = 'Black'
                        WHERE last = 'Red' AND first = 'Sue'""")

print(cursor.rowcount)

print('\nID, First, Last From Authors')
print(pd.read_sql("""SELECT id, first, last
            FROM authors""", connection, index_col=['id']))

cursor=cursor.execute("""DELETE FROM authors
                        WHERE id=6""")
print('\n',cursor.rowcount)

print('\nID, First, Last From Authors')
print(pd.read_sql("""SELECT id, first, last
            FROM authors""", connection, index_col=['id']))

connection.close()