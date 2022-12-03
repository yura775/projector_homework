"""""
3. Get a phrase from user input. Display whether the lenght of the string if longer than 5 characters, equal to 5 characters or shorter than 5 characters. Use if, elif, else for this.
"""""

str = input('Enter a phrase ')
if len(str) > 5:
    print('The phrase have more than 5 characters')
elif len(str) == 5:
    print('The phrase has 5 characters')
else:
    print('The phrase have less than 5 characters')

