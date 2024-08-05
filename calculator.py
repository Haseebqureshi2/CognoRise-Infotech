
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Please select operation: \n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n")

select = int(input())
 # Function to add two numbers
def add(num1, num2):
    return num1 + num2
 
# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2
 
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
 
# Function to divide two numbers
def divide(num1, num2):
    if (num2==0):

        print("Please Enter a valid number:")
    
    else:
        return num1 / num2
 
if select == 1:
    print(num1, "+", num2, "=",
                    add(num1, num2))
 
elif select == 2:
    print(num1, "-", num2, "=",
                    subtract(num1, num2))
 
elif select == 3:
    print(num1, "*", num2, "=",
                    multiply(num1, num2))
 
elif select == 4:
    print(num1, "/", num2, "=",
                    divide(num1, num2))
else:
    print("Invalid input")