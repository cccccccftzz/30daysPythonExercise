#Python Date Time

print("Catch up in Preview".center(80, "-"))
print("Time Objects to Represent Time".center(80, "-"))
import datetime
print(dir(datetime)) #dir()


from datetime import time
a = time()
print(f'{a = }') #This syntax cannot work, the output is a = datetime.time(0, 0)
print(f'{a}')

b = time(10, 30, 50) 
print(f'{b = }') #This syntax cannot work, the output is b = datetime.time(10, 30, 50)
print(f'{b}') #10:30:50, can directly to use b to print the time instead of the syntax above


c = time(hour = 10, minute = 30, second = 50)
print(f'{c}')

print("Using date from Datetime".center(80, "-"))
from datetime import date #Date is a class inside the datetime module
d = date(2024,2,4)
print(d)
print(f'Current date:', d.today()) #Output: Current date: 2024-02-06
#When using today() function, it only relates to the current date
today = date.today() #date is a class, today is a method
print(f'Current year: {today.year}')
print(f'Current month: {today.month}')
print(f'Current day: {today.day}')

print("Exercise 1".center(80, "-"))
print('Get the current day, month, year, hour, minute and timestamp from datetime module')
# import datetime 
#Datetime is a CLASS inside the Datetime Module
from datetime import datetime

now = datetime.now() #datetime is a class, .now() is a method
#The complete current timing

print(now) #2024-02-06 22:44:28.457600

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp() #Timestamp got '() cuz it is a function

print(f'{day = }')
print(f'{month = }')
print(f'{year = }')
print(f'{hour = }')
print(f'{minute = }')
print(f'{second = :02d}') #To keep digits result to be 'second = 06'
print(f'{timestamp = :.2f}') #timestamp = 1707231079.47

print(f'{day}/{month}/{year},{hour}:{minute}:{second:02d}') 
#6/2/2024,22:51:44

print("Exercise 2".center(80, "-"))
print(f'Format the current date using this format: "%m/%d/%Y, %H:%M:%S")')
now = datetime.now()
t = now.strftime('%m/%d/%Y, %a, %H:%M:%S')
print(f'time = {t}') 
#time = 02/06/2024, Tue, 23:14:14

print("Exercise 3".center(80, "-"))
print(f'Today is 5 December, 2019. Change this time string to time.')
date_string = '5 December, 2019'
print(f'{date_string = }')

date_object = datetime.strptime(date_string, '%d %B, %Y')
print(f'{date_object}') #2019-12-05 00:00:00

print("Exercise 4".center(80, "-"))
print(f'Calculate the time difference between now and new year.')
today = date.today() #date is a class, today is a method
cny = date(year = 2024, month = 2, day = 10)
time_left_for_cny = cny - today
print(f'{time_left_for_cny}')

print("Exercise 5".center(80, "-"))
print(f'Calculate the time difference between 1 January 1970 and now.')
#Method 1: Using date function
today = date.today()
target_date = date(1970, 1, 1)
time_to_target_date = today - target_date
print(f'{time_to_target_date}')

#Method 2: Using timedelta method
from datetime import timedelta
#class datetime.timedelta
#(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
t1 = timedelta(weeks = 2, days = 6)
t2 = timedelta(weeks = 2, days = 10)
print(t2 - t1)

print("Exercise 6".center(80, "-"))
print(f'To use datetime module for time series analysis')

#Calculate some counting days
today = date.today()
offical_date = date(2023, 11, 6)
valentine = date(2024, 2, 14)

print(f'{today-offical_date}')
print(f'{valentine-offical_date}')

#Generating a sequnce of dates
start_date = datetime(2024, 2, 7)
end_date = datetime(2024, 2, 12)
step = timedelta(days = 1) #How to define the day steps
current_date = start_date
while current_date <= end_date:
    print(current_date)
    current_date += step

print(f'To get a timestamp of any activities in an application')
time_start = datetime.now()
for i in range(1000000):
    pass
time_end = datetime.now()
duration = time_end - time_start
print(f'The duration of the activity is {duration}.')

print(f'Adding posts on a blog')
#ChatGPT method, havnet learnt the class so need review this later

class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.creation_timestamp = datetime.now()

    def display_post(self):
        formatted_timestamp = self.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S %p')
        print(f'Title: {self.title}')
        print(f'Content: {self.content}')
        print(f'Created on : {formatted_timestamp}\n')

post1 = BlogPost("Introduction to Python", "This is a blog post about Python programming.")
post2 = BlogPost("Data Science Basics", "Exploring the fundamentals of data science.")
#TypeError: BlogPost() takes no arguments

post1.display_post()
post2.display_post()
