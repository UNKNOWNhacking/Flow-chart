"""
square root (Newton Method)

Formula:
    0.5*(approx+n/approx)
"""
#ask a input to Enter a value

number = int(input("Enter a finding number : "))

#Creating a function

def Newton_sqrt(n) :

    #approx value is stored in approx_value variable

    approx_value = 0.5 * n

    #correct value is stored in final_value variable

    final_value = 0.5 * (approx_value + n / approx_value)
    
    #Creating a while loop
    #final_value and approx_value not satisfy execute a loop

    while final_value != approx_value :
        approx_value = final_value
        final_value = 0.5 * (approx_value + n / approx_value)

        #final_value and approx_value is same exit a loop

    return approx_value

    #return a approx_value


print("Given value is : ", number)

#Display a asked value 

#calling a function in print statement

print("The square is : ",Newton_sqrt(number))

#Display a square root value
