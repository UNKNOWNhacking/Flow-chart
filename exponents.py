"""
exponents in Python
"""

#create a variable named value and exponents

value = int(input("Enter a value : "))
exponents = int(input("Enter a Exponents : "))
spar = value # spar is stored value variable


#create a for loop in range fix a exponents value

for i in range(1, exponents):
    spar = spar * value

#Display a exponents value
print("exponents is : ", spar)
