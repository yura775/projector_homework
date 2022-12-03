"""""
Get a positive number from user input. Find all factors of this number.

Example:
If the number is 6, the factors are: 1, 2, 3, 6
If the number is 10, the factors are: 1, 2, 5, 10
"""""
num = int(input('Введіть число '))
factors = ''
for i in range(1, num+1):
    if num % i == 0:
        factors = factors +f'{i}, '
print(f'If the number is {num}, the factors are: {factors}')


