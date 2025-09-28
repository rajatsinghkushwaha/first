#factorial program using recursion
#This program starts here
'''
a=int(input("Enter the number for factorial: "))
def factorial(a):
    if (a<2):
        return 1
    else:
        return a*factorial(a-1)

result=factorial(a)
print("Factorial for the number is: ", result)
'''
#This program ends here

#factorial program using while loop
#This program starts here
'''
a=int(input("Enter the number for factorial: "))
if (a<2):
    print("Factorial for the number is: ", 1)
else:
    result=1
    while(a>=2):
          result=result*(a)
          a=a-1
    print("Factorial for the number is: ", result)
'''
#This program ends here

#factorial program using for loop
# This program starts here
'''
a=int(input("Enter the number for factorial: "))
if (a<2):
    print("Factorial for the number is: ", 1)
else:
    result=1
    for x in range(1,a+1):
           result=result*x
    print("Factorial for the number is: ", result)
'''
# This program ends here
