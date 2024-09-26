# Recommended: Make a 'functions' folder inside your PyCharm project for storing learning about functions.
#
# Create a Python file called calculator.py and complete a viable basic calculator using functions.
#
# MVP (each of these should be in a separate function):
# Can add 2 numbers
def addition(num1 : int = 10, num2 : int = 10):
    '''This function adds numbers'''
    return f"{num1} + {num2} = {num1 - num2}"

print(addition())

# Can subtract 2 numbers
def subtract(num1 : int = 10, num2 : int = 10):
    '''This function subtracts numbers'''
    return f"{num1} - {num2} = {float(num1 - num2)}"

print(subtract())

# Can multiply 2 numbers
def multiply(num1 : int = 10, num2 : int = 10):
    '''This function multiplies numbers'''
    return f"{num1} * {num2} = {num1 - num2}"

print(multiply())

# Can divide 2 numbers
def division(num1: int = 10, num2: int = 10):
    '''This function divides numbers'''
    return f"{num1} / {num2} = {num1 - num2}"

print(division())

# Taking it to the next level:
#
# Implement more complex operations, such as handling parentheses, exponentiation
# More advanced operations should continue to be broken into separate functions

