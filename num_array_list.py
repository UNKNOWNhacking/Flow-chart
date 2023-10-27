"""
Python Program to Find Sum of Array
"""
#Display hint

print("Enter a Value like this example\n","\tExample\n", "\t1 2 3 4")

#create a list 
#split(), map()

list = list(map(int,input("Enter a Value : ").split()))

#create a variable named sum

sum = 0

#create a for loop

for element in list:
    sum = sum + element

#Display a result
print("result :",sum)

