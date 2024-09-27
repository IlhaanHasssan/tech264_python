from math_operations import *
# we have imported a module (single file imported)
# a library is a set of modules
# packages are different because they are installable
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Exponentiation\n5. Division")
user_input = input("Enter which math operator you would like to use (1-5): ")


#Addition
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
if user_input == "1":
    result = add(first_num, second_num)
    print(f"{first_num} + {second_num} = {result}")
#Subtractio
elif user_input == "2":
    result = subtract(first_num, second_num)
    print(f"{first_num} - {second_num} = {result}")

#Multiiplication
elif user_input == "3":
    result = multiply(first_num, second_num)
    print(f"{first_num} * {second_num} = {result}")

#Exponentiation
elif user_input == "4":
    result = exponentiation(first_num, second_num)
    print(f"{first_num} ⌃ {second_num} = {result}")

#Division
elif user_input == "5":
    if second_num != 0:
        result = divide(first_num, second_num)
        print(f"{first_num} / {second_num} = {result}")
    else:
        print("Error! Cannot divide by 0")

else:
    print("Invalid input! You must choose one of the 5 options")