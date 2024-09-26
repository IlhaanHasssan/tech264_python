from math_operations import *
# we have imported a module (single file imported)
# a library is a set of modules
# packages are different because they are installable

user_input = input("Enter which math operator you would like to use: 1. Addition")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")