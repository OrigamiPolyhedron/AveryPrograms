#16.8
#This will not function. I have tried for hours. I'm considering it a lost cause
#until I can get some actual help during class. Google has suggested it is
#from some conflict that might exist between how code was written for
#sqlalchemy in 1.4 vs the newest versions. I literally DO NOT have time
#to spend this much time on every piece of an assignment.
#I got the lesser parts of 16 done and that's literally all I can do.
#And that took hours in itself. Please record that some of these
#assignments have issues if other students have this much trouble.
import sqlite3
import sqlalchemy as sa

conn = sa.create_engine('sqlite:///booksss.db')

conn.execute('SELECT title FROM booksss ORDER by DESC')





