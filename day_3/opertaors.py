# Day 2: 30 Days of python programming

import math

# ======> Exercises

# ======> 1: Declare an integer variable for Age
age = 27

# ======> 2: Declare a float variable for Height
height = 1.68

# ======> 3: Declare a complex variable for a complex number
complex_number = 3 - 7j

# ======> 4: Calculate the area of a triangle using inputs for base and height
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is ", area)

# ======> 5: Calculate the perimeter of a triangle using inputs for the lengths of the three sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is ", perimeter)

# ======> 6: Calculate the area and perimeter of a rectangle using inputs for length and width
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is ", area)
print("The perimeter of the rectangle is ", perimeter)

# ======> 7: Calculate the area and circumference of a circle using inputs for the radius
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print("The area of the circle is ", area)
print("The circumference of the circle is ", circumference)

# ======> 8: Calculate the slope of y = 2x - 2
slope = 2  # Coefficient of x in the equation y = 2x - 2
y_intercept = -2
x_intercept = -y_intercept / slope
print("The slope of y = 2x - 2 at x = ", x_intercept, " is ", slope)
print("The y-intercept is ", y_intercept)
print("The x-intercept is ", x_intercept)

# ======> 9: Find the slope and euclidean distance between (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope1 = (y2 - y1) / (x2 - x1)
# euclidean_distance = math.hypot(x2 - x1, y2 - y1) # or using the formula
euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("The slope between (2, 2) and (6, 10) is ", slope1)
print("The Euclidean distance between (2, 2) and (6, 10) is ", euclidean_distance)

# ======> 10: Compare the slopes in tasks 8 and 9.
print("The slope from task 8 is ", slope)
print("The slope from task 9 is ", slope1)
print("Are the slopes equal? ", slope == slope1)

# ======> 11: Calculate y = x² + 6x + 9 for Various x and When y = 0.

print("Calculate y = x² + 6x + 9 for x from -10 to 10")
print("x: -10, y:", (-10)**2 + 6*(-10) + 9)
print("x: -9, y:", (-9)**2 + 6*(-9) + 9)
print("x: -8, y:", (-8)**2 + 6*(-8) + 9)
print("x: -7, y:", (-7)**2 + 6*(-7) + 9)
print("x: -6, y:", (-6)**2 + 6*(-6) + 9)
print("x: -5, y:", (-5)**2 + 6*(-5) + 9)
print("x: -4, y:", (-4)**2 + 6*(-4) + 9)
print("x: -3, y:", (-3)**2 + 6*(-3) + 9, "<-- When y = 0")
print("x: -2, y:", (-2)**2 + 6*(-2) + 9)
print("x: -1, y:", (-1)**2 + 6*(-1) + 9)
print("x: 0, y:", 0**2 + 6*0 + 9)
print("x: 1, y:", 1**2 + 6*1 + 9)
print("x: 2, y:", 2**2 + 6*2 + 9)
print("x: 3, y:", 3**2 + 6*3 + 9)
print("x: 4, y:", 4**2 + 6*4 + 9)
print("x: 5, y:", 5**2 + 6*5 + 9)
print("x: 6, y:", 6**2 + 6*6 + 9)
print("x: 7, y:", 7**2 + 6*7 + 9)
print("x: 8, y:", 8**2 + 6*8 + 9)
print("x: 9, y:", 9**2 + 6*9 + 9)
print("x: 10, y:", 10**2 + 6*10 + 9)

# ======> 12: Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = "python"
dragon = "dragon"
len_python = len(python)
len_dragon = len(dragon)
print("Length of 'python': ", len_python)
print("Length of 'dragon': ", len_dragon)
print("Are the lengths equal? ", len_python == len_dragon)

# ======> 13: Check if 'on' is in both words
print("Is 'on' in both words? ", 'on' in python and 'on' in dragon)

# ======> 14: Use in with sentence
sentence = "I hope this course is not full of jargon."
print("'jargon' in sentence: ", sentence, ' ? ', 'jargon' in sentence)

# ======> 15: Check if 'on' not in both words
print("Is 'on' not in both words", python, " and ", dragon, " ? ", 'on' not in python and 'on' not in dragon)

# ======> 16: Convert length of text to float and then to string
text = "python"
len_text = float(len(text))
print("Length of text as float: ", len_text)
print("Length of text as string: ", str(len_text))

# ======> 17: Check If a Number Is Even
number = int(input("Enter a number: "))
is_even = number % 2 == 0
print("Is the number", number, "even? ", is_even)

# ======> 18: Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division = 7 // 3
int_value = int(2.7)
print("Is the floor division of 7 by 3 equal to the int converted value of 2.7? ", floor_division == int_value)

# ======> 19: Check if type of '10' is equal to type of 10
print("Is the type of '10' equal to the type of 10? ", type('10') == type(10))

# ======> 20: Check if int('9.8') is equal to 10
print("Is int('9.8') equal to 10? ", int('9.8') == 10)

# ======> 21: Script to calculate weekly earnings
hours_worked = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))
weekly_earnings = hours_worked * hourly_rate
print("Weekly earnings: ", weekly_earnings)

# ======> 22: Script to calculate number of seconds lived
age = int(input("Enter your age in years: "))
seconds_lived = age * 365 * 24 * 60 * 60
print("You have lived for approximately", seconds_lived, "seconds.")

# ======> 23: Python script to display the following table
# 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# for i in range(1, 6):
#     print(i, 1, i, i**2, i**3)

print(1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
