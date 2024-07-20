#13.1 Write the current date as a string to the text file today.txt
#This means having some code that takes the current date and sends
#it as a string to a text file called "today.txt"

#13.2 Read the text file today.txt into the string today_string.

#13.3 Parse the date from today_string.

#15.1 Use multiprocessing to create three separate processes. Make each
#one wait a random number of seconds between zero and one, print the current
#time, and then exit.
#13.1
from datetime import date

currentDate = date.today()

currentDate

#code for testing that it does so
#print(str(currentDate))
f = open("today.txt", "w")
f.write(str(currentDate))
f.close()

#13.2
with open("today.txt", "r") as f:
    today_string = f.read().rstrip()
f.close()
print(today_string)
print("This date came from the today.txt and is stored in today_string")

#13.3
from datetime import date
from datetime import datetime
datetime_object = datetime.strptime(today_string, "%Y-%m-%d")

date_object = datetime_object.date()

year = date_object.year
print("The year is: ", year)

month = date_object.month
print("The month is: ", month)

day = date_object.day
print("The day is: ", day)


#15.1
#processing thing
import random
import time
import multiprocessing
from datetime import datetime
#This code demostrates the random wait time to run code part. It also demostrates the print current time part.
t = random.uniform(0, 1)
time.sleep(t)
time1 = datetime.now()
current_time1 = time1.strftime("%H:%M:%S")
print("Current Time =", current_time1)

''' The following is some leftover code from when I tried to do part of 15.1
def print_current_time():
    t = random.uniform(0, 1)
    time.sleep(t)
    time1 = datetime.now()
    current_time1 = time1.strftime("%H:%M:%S")
    print("Current Time =", current_time1)

'''