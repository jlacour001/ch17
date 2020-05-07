"""
The purpose of this program is to complete exercise
17.1 on page 799 in one complete script.
I have added print statements for clarity.

Author: Jacques LaCour
Date: 05/06/2020
"""

import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.options.display.max_columns=10

# Select all author's last names from the Authors table in descending order
print("STEP 1:")
print(pd.read_sql("""SELECT last
            FROM authors
            ORDER BY last DESC""", connection))

# Select all titles from the Titles table in ascending order
print("\n\nSTEP 2:")
print(pd.read_sql("""SELECT title
            FROM titles
            ORDER BY title ASC""", connection))

# Use INNER JOIN to select books of certain author
# Incl. title, copyright year, and ISBN
# Order alphabetically by title
print("\n\nSTEP 3:")
print(pd.read_sql("""SELECT id, author_ISBN.isbn, title, copyright
                    FROM author_ISBN
                    INNER JOIN titles
                    ON author_ISBN.isbn = titles.isbn
                    WHERE id=1""", connection, index_col=['id']))

# Insert a new author into the authors table
print("\n\nSTEP 4:")
cursor=connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (id, first, last)
                        VALUES ('6', 'Michael','Crichton')""")
print(pd.read_sql("""SELECT last
            FROM authors
            ORDER BY last DESC""", connection))

# Insert a new title for an author, book must have entry in author_ISBN and in titles
print("\n\nSTEP 5:")
cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright) 
                        VALUES ('9780345538987','Jurassic Park','1','1990')""")
cursor = cursor.execute("""INSERT INTO author_ISBN ('id', 'isbn')
                        VALUES ('6', '9780345538987')""")
print(pd.read_sql("""SELECT *
                    FROM titles
                    ORDER BY title ASC""", connection))

# END PROGRAM