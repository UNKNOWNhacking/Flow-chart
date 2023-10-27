"""
GCD of Two numbers in Python.
"""

#create a function named Gcd

def Gcd(value1, value2):

    #create a if condision 
    #this condision satisfy this block of code execute

    if value2 == 0:
        return value1

    #not satisfy this block of code execute

    else:
        return Gcd(value2, value1 % value2)


#create two variable value1 and value2

value1 = int(input("Enter Value1 : "))
value2 = int(input("Enter Value2 : "))

#calling function stored in variable
gcd = Gcd(value1, value2)

#Display a gcd value
print("The gcd value is :", gcd)
