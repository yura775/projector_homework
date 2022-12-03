"""""
5. Write a Python program to check a triangle is equilateral, isosceles or scalene. Get all three sides from user input.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
"""""

x, y, z = int(input('Enter first side ')), int(input('Enter second side ')), int(input('Enter third side '))

if x == y == z:
    print('The triangle is equilateral')
elif x != y != z:
    print('The triangle is scalene')
else:
    print('The triangle is isosceles')


