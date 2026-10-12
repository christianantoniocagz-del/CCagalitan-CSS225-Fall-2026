""""
Christian Antonio Cagalitan 10/11/2026
"""
import math

# Problem 1– Write a program that prints “Hello World” to the screen.

print("Hello World")

# Problem 2 – Write a program that asks the user for their name and greets them with their name.

userName1=input("What is your name ?") # Takes users name.
print("Hello, ",userName1)

# Problem 3 - Modify the previous program such that only the users you and your instructor are greeted with their names.

userName2=input("What is your name ?")# Takes users name.

if userName2.lower()=="christian" or userName2.lower()== "antonio":# Checks if the users name is mine or professors even if its capitalised or not.

    print("Hello",userName2)

#Problem 4 - Write a program that will compute the area of a circle.
#Prompt the user to enter the radius and print a nice message back to the user with the answer.

radius = float(input("Enter the radius of the circle: "))# Asks the user to enter the radius.

area = math.pi * (radius ** 2) # Calculates the area using π * r^2

print("The area of the circle is: ",area)

#Problem 5 - Write a program that will compute MPG for a car. Prompt the user to enter the
#number of miles driven and the number of gallons used. Print a nice message with the answer.

milesDriven = float(input("Enter the number of miles driven: "))# Takes users miles

gallonsUsed = float(input("Enter the number of gallons used: "))# Takes users gallons used

mpg = milesDriven/gallonsUsed# calculates miles per gallon

print(f"Your miles per gallon on this trip is {mpg:.2f}") # Prints the mpg with a rounded value

# Problem 6 - Write a program that will convert degrees Fahrenheit to degrees Celsius.

fahrenheit=float(input("Enter the temperature in Fahrenheit: "))# Takes user fahrenheit.

fToCelsius=(fahrenheit - 32) * (5 / 9)# converts fahrenheit to celsius using formula C = (F-32)x(5/9).

print(f" {fahrenheit:.1f}°F is equal to {fToCelsius:.1f}°C.")# Prints fahrenheit and celsius with rounded value.

"""
Problem 7 - It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is
Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you
return home after 10 nights you would return home on a Saturday (day 6) Write a general
version of the program which asks for the starting day number, and the length of your stay, and
it will tell you the number of day of the week you will return on.
"""


dayList="Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"

startDay = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): ")) # Asks user for start day

stayLength = int(input("Enter the number of nights you will stay: ")) # Asks users for lenght of their stay

returnDay = (startDay + stayLength) % 7 # Calculates return date using the modulo

print("You will return on ",dayList[returnDay]) # Prints day they return by reffering to a value in day list using the returnDay variable
