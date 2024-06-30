#16.4 books became booksss due to some leftover class work interference and other mistakes.
#Use the sqlite3 module to create a SQLite database called
#books.db and a table called books with these 
#fields: title (text), author (text), and year (integer)
#16.5 is done here as well

import sqlite3
import pandas as pd

df = pd.read_csv("books2.csv")
#connection
con = sqlite3.connect("booksss.db")
#cursor
cur = con.cursor()
#table creation for the data
cur.execute("CREATE TABLE booksss('title', 'author', 'pubyear')")

#data into table
data_rows = df.values.tolist()

data_to_add = [(d_row[0], d_row[1], d_row[2]) for d_row in data_rows]

cur.executemany("INSERT INTO booksss VALUES(?, ?, ?)", data_to_add)

#commit changes
con.commit()

#Close connection
con.close()





