#1: Create a Module:

def add(a, b):
    #returns the sum of a and b

    return (a + b)

def subtract(a, b):
    #returns the difference between a and b
    return a - b 

def multiply(a, b):
    #return the product of a and b
    return a * b

def divide(a,b):
    #retunrs the quotient of a divided by b. 
    if b == 0:
        print("error. cannot divide by zero.")
        return None
    return a / b 


