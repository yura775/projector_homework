"""""
Get a number from user input and iterate from 0 to that number.

Print 'foo' if the number is divisible by 3.
Print 'bar' if the number is divisible by 5.
Print 'foobar' if the number is divisible by both 3 and 5.
"""""
for i in range(int(input('Enter the number '))):
    if i % 3 and i % 5 == 0:
        print('foobar')
    elif i % 3 == 0:
        print('foo')
    elif i % 5 == 0:
        print('bar')
    else:
        print(i)
