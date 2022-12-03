"""""
Write a program that takes number as its input and doubles that number few times in a loop. Number of iterations and initial number should be taken from user input. You should display each result on a separate line. Here is some sample output:
Input:
initial number: 2
number of iterations: 5

Output:
4
8
16
32
64
"""""

a, b = int(input('Enter first digit ')), int(input('Enter second digit '))
for i in range(b):
    a=a*2
    print(a)