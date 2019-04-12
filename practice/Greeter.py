import datetime
import sys
from math import pi

print()

print("hello world")

print(5 * 6)

x = 20
print(x)

first_bool = True
print(first_bool)

first_word = "hehe"
print(first_word)

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a "
      "diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!\n")

print(sys.version.__str__() + "\n")
print(sys.version_info.__str__() + "\n")

print(str(datetime.datetime.now()))

# This is my first python program <3
r = float(input("Input the radius of a circle: "))
print("The area of the cirlce with radius " + str(r) + " is: " + str(pi * r ** 2))

cs_input = str(input("Enter a list of comma seperated numbers: "))
cs_list = cs_input.split(",")
cs_tuple = tuple(cs_list)
print(str(cs_list))
print(str(cs_tuple))
