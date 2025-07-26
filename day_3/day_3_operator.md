# Day 3 - 30DaysOfPython Challenge

Welcome to Day 3 of the 30DaysOfPython Challenge! Today is all about operators — arithmetic operators, comparison operators, logical operators, and practical applications in geometry, algebra, and string manipulation.

## Tasks for Day 3

### Level 1: Basic Variable Declarations

1. **Project Structure**
   Create a folder named `day_3` inside the `30DaysOfPython` project and a file called `operators.py`.

2. **Python Comment**
   Add a comment at the top of the file:

   ```python
   # Day 3: 30 Days of python programming
   ```

3. **Import Math Module**
   Import the math module for advanced mathematical operations:

   ```python
   import math
   ```

4. **Variable Declarations**
   Declare and assign values to the following variables:

   ```python
   age = 27
   height = 1.68
   complex_number = 3 - 7j
   ```

### Level 2: Geometric Calculations

1. **Triangle Area Calculation**
   Calculate the area of a triangle using inputs for base and height:

   ```python
   base = float(input("Enter base: "))
   height = float(input("Enter height: "))
   area = 0.5 * base * height
   print("The area of the triangle is ", area)
   ```

2. **Triangle Perimeter Calculation**
   Calculate the perimeter of a triangle using inputs for the lengths of the three sides:

   ```python
   a = float(input("Enter side a: "))
   b = float(input("Enter side b: "))
   c = float(input("Enter side c: "))
   perimeter = a + b + c
   print("The perimeter of the triangle is ", perimeter)
   ```

3. **Rectangle Area and Perimeter**
   Calculate the area and perimeter of a rectangle using inputs for length and width:

   ```python
   length = float(input("Enter length: "))
   width = float(input("Enter width: "))
   area = length * width
   perimeter = 2 * (length + width)
   print("The area of the rectangle is ", area)
   print("The perimeter of the rectangle is ", perimeter)
   ```

4. **Circle Area and Circumference**
   Calculate the area and circumference of a circle using inputs for the radius:

   ```python
   radius = float(input("Enter radius: "))
   pi = 3.14
   area = pi * radius ** 2
   circumference = 2 * pi * radius
   print("The area of the circle is ", area)
   print("The circumference of the circle is ", circumference)
   ```

### Level 3: Algebraic Operations

1. **Linear Equation Analysis**
   Calculate the slope and intercepts of the equation y = 2x - 2:

   ```python
   slope = 2  # Coefficient of x in the equation y = 2x - 2
   y_intercept = -2
   x_intercept = -y_intercept / slope
   print("The slope of y = 2x - 2 at x = ", x_intercept, " is ", slope)
   print("The y-intercept is ", y_intercept)
   print("The x-intercept is ", x_intercept)
   ```

2. **Slope and Distance Between Points**
   Find the slope and euclidean distance between two points:

   ```python
   x1, y1 = 2, 2
   x2, y2 = 6, 10
   slope1 = (y2 - y1) / (x2 - x1)
   euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
   print("The slope between (2, 2) and (6, 10) is ", slope1)
   print("The Euclidean distance between (2, 2) and (6, 10) is ", euclidean_distance)
   ```

3. **Slope Comparison**
   Compare the slopes from different calculations:

   ```python
   print("The slope from task 8 is ", slope)
   print("The slope from task 9 is ", slope1)
   print("Are the slopes equal? ", slope == slope1)
   ```

4. **Quadratic Function Evaluation**
   Calculate y = x² + 6x + 9 for various x values and find when y = 0:

   ```python
   print("Calculate y = x² + 6x + 9 for x from -10 to 10")
   print("x: -10, y:", (-10)**2 + 6*(-10) + 9)
   print("x: -9, y:", (-9)**2 + 6*(-9) + 9)
   # ... continue for all values
   print("x: -3, y:", (-3)**2 + 6*(-3) + 9, "<-- When y = 0")
   ```

### Level 4: String Operations and Comparisons

1. **String Length Comparison**
   Find the length of 'python' and 'dragon' and make a comparison:

   ```python
   python = "python"
   dragon = "dragon"
   len_python = len(python)
   len_dragon = len(dragon)
   print("Length of 'python': ", len_python)
   print("Length of 'dragon': ", len_dragon)
   print("Are the lengths equal? ", len_python == len_dragon)
   ```

2. **String Membership Testing**
   Check if 'on' is in both words:

   ```python
   print("Is 'on' in both words? ", 'on' in python and 'on' in dragon)
   ```

3. **Sentence Analysis**
   Use the `in` operator with a sentence:

   ```python
   sentence = "I hope this course is not full of jargon."
   print("'jargon' in sentence: ", sentence, ' ? ', 'jargon' in sentence)
   ```

4. **Negative Membership Testing**
   Check if 'on' is not in both words:

   ```python
   print("Is 'on' not in both words", python, " and ", dragon, " ? ", 'on' not in python and 'on' not in dragon)
   ```

### Level 5: Type Conversion and Type Checking

1. **Type Conversion Operations**
   Convert length of text to float and then to string:

   ```python
   text = "python"
   len_text = float(len(text))
   print("Length of text as float: ", len_text)
   print("Length of text as string: ", str(len_text))
   ```

2. **Even Number Detection**
   Check if a number is even using the modulo operator:

   ```python
   number = int(input("Enter a number: "))
   is_even = number % 2 == 0
   print("Is the number", number, "even? ", is_even)
   ```

3. **Floor Division Comparison**
   Check if the floor division of 7 by 3 is equal to the int converted value of 2.7:

   ```python
   floor_division = 7 // 3
   int_value = int(2.7)
   print("Is the floor division of 7 by 3 equal to the int converted value of 2.7? ", floor_division == int_value)
   ```

4. **Type Comparison**
   Check if type of '10' is equal to type of 10:

   ```python
   print("Is the type of '10' equal to the type of 10? ", type('10') == type(10))
   ```

5. **String to Integer Conversion**
   Check if int('9.8') is equal to 10:

   ```python
   print("Is int('9.8') equal to 10? ", int('9.8') == 10)
   ```

### Level 6: Practical Applications

1. **Weekly Earnings Calculator**
   Script to calculate weekly earnings:

   ```python
   hours_worked = int(input("Enter the number of hours worked: "))
   hourly_rate = float(input("Enter the hourly rate: "))
   weekly_earnings = hours_worked * hourly_rate
   print("Weekly earnings: ", weekly_earnings)
   ```

2. **Seconds Lived Calculator**
   Script to calculate number of seconds lived:

   ```python
   age = int(input("Enter your age in years: "))
   seconds_lived = age * 365 * 24 * 60 * 60
   print("You have lived for approximately", seconds_lived, "seconds.")
   ```

3. **Mathematical Table Display**
   Python script to display a mathematical table:

   ```python
   print(1, 1, 1, 1)
   print(2, 1, 2, 4, 8)
   print(3, 1, 3, 9, 27)
   print(4, 1, 4, 16, 64)
   print(5, 1, 5, 25, 125)
   ```

## Key Concepts Covered

### Arithmetic Operators

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Floor Division (`//`)
- Modulo (`%`)
- Exponentiation (`**`)

### Comparison Operators

- Equal (`==`)
- Not Equal (`!=`)
- Greater Than (`>`)
- Less Than (`<`)
- Greater Than or Equal (`>=`)
- Less Than or Equal (`<=`)

### Logical Operators

- AND (`and`)
- OR (`or`)
- NOT (`not`)

### Membership Operators

- IN (`in`)
- NOT IN (`not in`)

### Type Conversion Functions

- `int()`
- `float()`
- `str()`
- `type()`

### Mathematical Functions

- `math.sqrt()` for square root
- `math.hypot()` for hypotenuse calculation
- `len()` for string length

This day covers fundamental operators and their practical applications in geometry, algebra, and string manipulation, providing a solid foundation for more complex programming tasks.
