# *Python Learning:*
* [Git](..%2Flearning_git%2FREADME.md)
* [Markdown](..%2Flearning_markdown%2FREADME.md)

```python
# What is a variable?
# A variable is a container to store data
# It is called a variable because it is a symbolic name that is a reference/pointer to an object
#eg: x = 5, x is the variable name pointing to the int object 5
import time

a = 30
b = 10.5
z = "Ilhaan"
x = 15

print(type(a))
print(type(b))
print(type(z))
print(a)
print(id(a))

# == is an equality operator for booleans meaning it returns true or false.
#it does this by checking if the two operands are equal

#Explain: What's the difference between a dynamically typed language (like Python) and a strong typed language ?
# Type-checking (determining data types) happens during run-time for python vs before the program runs
#Dynamicallt typed languages allow for more flexibility
#you can add an int to a float in python without error
# the id of the variable changes because the unique identifier for the specified object is based on the value

x = 5
y = 1
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)

i = 50
print(type(i))
#numeric data type
j = 100.5
print(type(j))
#float data type
print(type(j == i))
#boolean data type

One_third = 1/3
print(One_third)
print(One_third * 3)
#python has internal rounding of integers due to IEEE754 arithmetic

print(bool(""))
# empty string is false
print(bool("Hello"))
#string with a value is true

null = None
print(type(null))
#none in python denotes the absence of a value
#commonly used to represent the absence of a value in str data type but not the same as an empty string
#can be used in boolean
#JS = null, Java = void

print(null is None)


hi = "Hello World!"
print(hi.isalpha()) #checks if it is made up of all letters
print(hi.islower()) #checks if all letters are lowercase
print(hi.isupper()) #checks if all letters are uppercase
print(hi.istitle()) #checks if first letter is capital

name = "Ilhaan"
age = 1000
DOB = "14.03.1999"
print(name, age, DOB)
#input("name, age and DOB =")

age_int = 100
name_str = "Ilhaan"

age_calc = 2024 - age_int
print(age_calc)
print("OMG, you are " + str(age_int) + " years old so you were born in " + str(age_calc))


age_int = input("age = ")
name_str = input("name = ")
print(age_int)
print(name_str)

```



