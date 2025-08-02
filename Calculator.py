## PLP week 1 Assisgment 
## Task: Basic calculator
## Objective: the user should be able to input data and the system to calculate the output
##
import math
x = float(input("First Number:")) # This fetchs the first data from the user
y = float(input("Second Number:")) # This fetchs the second data from the user

operation = input("What calculation do you want to perform (+, -, *, /): ") # This make sure the user to select the data requred by the user

if operation == '+' :
    result = x + y #Addition calculation
    print(f"{x} {operation} {y} = {result}") #Output
elif operation == '/':
    result= x / y # Division
    print(f"{x} {operation} {y} = {result}") #Output
elif operation == '*':
    result = x * y  # Multiplication
    print(f"{x} {operation} {y} = {result}") #Output
elif operation == '-':
    result = x - y   # subtraction
    print(f"{x} {operation} {y} = {result}") #Output
else :
    print('You enter a wrong input') # Err Messege



