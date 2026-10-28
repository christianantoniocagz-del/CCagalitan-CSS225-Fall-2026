# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020: # Alternative code: 1900 < year < 2020
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")

"""
Errors caused by:
Line 9: 
1. "==" on year variable : Logic Error
2. int() function is missing a closing parenthesis: Syntax Error

Line 11:
1. Missing : at the end of the if statement: Syntax Error

Line 13:
1. && is used instead of and in Python: Syntax Error
2. Missing : at the end of the elif statement: Syntax Error

Line 14
1.elif is missing a condition: Syntax Error. Use else: if you want to catch all remaining cases.
"""

