"""""
Write a program that caluculate Fibonacci series. The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers. The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on. Number of iterations should be taken from user input.
"""""

num= int(input('Enter the number of eterations '))
n1, n2 = 1, 1
count = 0
sequence = ""
if num <= 0:
   print("wrong number of eterations")

elif num == 1:
   print(n1)
# generate fibonacci sequence
else:
   while count < num:
       sequence = sequence +f'{n1}, '
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print(sequence)
