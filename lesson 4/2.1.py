"""""
Write a Python program that reads two integers representing a month and prints the season for that month. Get month from the user input.

Expected Output:
Input the month: october
Season is autumn
"""""

month= input("Enter the month ")

match month.lower():
    case 'december' | 'january' | 'february':
        print('Season is winter')
    case 'march' | 'april' | 'may':
        print('Season is spring')
    case 'june' | 'july' | 'august':
        print('Season is summer')
    case 'september' | 'october' | 'november':
        print('Season is fall')
    case _ :
        print('Try again!')