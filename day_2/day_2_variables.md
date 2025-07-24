# Day 2 - 30DaysOfPython Challenge

Welcome to Day 2 of the 30DaysOfPython Challenge! Today is all about variables — declaring, assigning, checking data types, performing operations, and understanding more about Python's behavior with different types of data.

## Tasks for Day 2

### Level 1

1. **Project Structure**
   Create a folder named ``day_2`` inside the ``30DaysOfPython`` project and a file called ``variables.py``.

2. **Python Comment**
   Add a comment at the top of the file:

   ```python
   # Day 2: 30 Days of python programming
   ```

3. **Variable Declarations**
   Declare and assign values to the following variables:

   ```python
   first_name = "John"
   last_name = "Doe"
   full_name = first_name + " " + last_name
   country = "Togo"
   city = "Lomé"
   age = 28
   year = 2025
   is_married = False
   is_true = True
   is_light_on = True
   ```

4. **Multiple Variable Assignment**
   Assign multiple values in one line:

   ```python
   x, y, z = 1, 2, 3
   ```

### Level 2

1. **Check Data Types**
   Use the type() function to check the types of all your variables:

   ```python
   print("Type of first_name:", type(first_name))
   print("Type of last_name:", type(last_name))
   print("Type of full_name:", type(full_name))
   print("Type of country:", type(country))
   print("Type of city:", type(city))
   print("Type of age:", type(age))
   print("Type of year:", type(year))
   print("Type of is_married:", type(is_married))
   print("Type of is_true:", type(is_true))
   print("Type of is_light_on:", type(is_light_on))
   print("Type of x:", type(x))
   print("Type of y:", type(y))
   print("Type of z:", type(z))
   ```

2. ****Length of First Name**
   Use len() to check how many characters are in your first name:

   ```python
   print("Length of first_name:", len(first_name))
   ```

3. **Compare Name Lengths**
   Compare the lengths of your first and last name:

   ```python
   print("Is first_name longer than last_name?", len(first_name) > len(last_name))
   print("Length difference:", abs(len(first_name) - len(last_name)))
   ```

4. **Arithmetic with Numbers**
   Declare two numbers and perform operations:

   ```python
   num_one = 5
   num_two = 4

   total = num_one + num_two
   diff = num_one - num_two
   product = num_one * num_two
   division = num_one / num_two
   remainder = num_two % num_one
   exp = num_one ** num_two
   floor_division = num_one // num_two

   print("Total:", total)
   print("Difference:", diff)
   print("Product:", product)
   print("Division:", division)
   print("Remainder:", remainder)
   print("Exponentiation:", exp)
   print("Floor Division:", floor_division)
   ```
