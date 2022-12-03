"""""
Write a program that takes a number as input and revert it using math operators. You might use result of the exercise from the first lesson. Here you should be able to do it not only for three-digit numbers, but for any numbers.
"""""

num = int(input("Enter the number "))
reversed = 0
while (num > 0):
    remainder = num % 10
    reversed = (reversed * 10) + remainder
    num = num // 10

print(f"The reverse number is {reversed}")