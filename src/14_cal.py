"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

month_options = [*range(1, 12)]

# set first day of the week to Sunday (originally Monday)
calendar.setfirstweekday(calendar.SUNDAY)

user_month = input('Month: ')
user_year = input('Year: ')

today = datetime.today()

# # will print in calendar format
# if user_month == '' and user_year == '':
#     print('1st one invoked')
#     for week in calendar.monthcalendar(today.year, today.month):
#         print(week)
# elif int(user_month) in month_options and user_year == '':
#     print('2nd one invoked')
#     for week in calendar.monthcalendar(today.year, int(user_month)):
#         print(week)
# elif int(user_month) in month_options and int(user_year) > 0:
#     print('3rd one invoked')
#     for week in calendar.monthcalendar(int(user_year), int(user_month)):
#         print(week)
# else:
#     print("Month should be formatted as whole integers (1-12); Years must be formatted to 4 digits (ex. 2019)")

# will print in calendar format
# if both inputs are not filled
if user_month == '' and user_year == '':
    # print('1st one invoked')
    for week in calendar.monthcalendar(today.year, today.month):
        print(week)
elif user_month != '':
    # if only the month input is filled
    if int(user_month) in month_options and user_year == '':
        # print('2nd one invoked')
        for week in calendar.monthcalendar(today.year, int(user_month)):
            print(week)
    # if both fields are inputted
    elif int(user_month) in month_options and int(user_year) > 0:
        # print('3rd one invoked')
        for week in calendar.monthcalendar(int(user_year), int(user_month)):
            print(week)
else:
    print("Month should be formatted as whole integers (1-12); Years must be formatted to 4 digits (ex. 2019)")