from math_operations import *
# we have imported a module (single file imported)
# a library is a set of modules
# packages are different because they are installable

user_input = input("Enter which math operator you would like to use: 1. Addition 2.Subtraction 3.Multiplication 4.Division: ")

#Addition
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
if user_input == "1":
    result = add(first_num, second_num)
    print(f"{first_num} + {second_num} = {result}")
#Subtraction
elif user_input == "2":
    result = subtract(first_num, second_num)
    print(f"{first_num} - {second_num} = {result}")

#Multiiplication
elif user_input == "3":
    result = multiply(first_num, second_num)
    print(f"{first_num} * {second_num} = {result}")

#Division
#Division
elif user_input == "4":
    if second_num != 0:
        result = divide(first_num, second_num)
        print(f"{first_num} / {second_num} = {result}")
    else:
        print("Error! Cannot divide by 0")

else:
    print("Invalid input! You must choose one of the 4 options")