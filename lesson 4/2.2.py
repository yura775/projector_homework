"""""
2. Write a Python program to get next day of a given date. Get day, month and year from the user input.
Expected Output:
**Input a year:** 2022                                                     
**Input a month [1-12]:** 8                                               
**Input a day [1-31]:** 23                                           
The next date is [yyyy-mm-dd] 2022-8-24
"""""
month_length = 0
year= int(input('Enter the year '))
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input('Enter the month '))
try:
    if month > 12:
        print('There are no such month. Please restart the program.')
        month = int(input('Enter the month '))

    elif month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    elif month in (2, 4, 6, 9, 11):
        month_length = 30
except:
    print('something went wrong. Please restart the program')

day = int(input('Enter the day '))
try:
    if day > 31:
        print('There are no such date. Please restart the program')

    elif day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
except:
        print('something went wrong. Try again later')

print(f"The next date is {day}.{month}.{year}")
