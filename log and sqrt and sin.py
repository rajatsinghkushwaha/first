# This program will calculate log, sin in radian and square of a number given by the user
#For calculating all this math module in imported in this program

import math as m
a=float(input("Please enter the number: "))
print("The square of a number is: " ,m.sqrt(a))
print("The sin value in radian is:" ,m.sin((m.radians(a))))
print("The log of a number is:" ,m.log(a))