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
#Dynamically typed languages allow for more flexibility
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
#floating-point arithmetic is subject to precision limits
#so you should be careful when working with floating-point numbers in critical calculations

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

age_int = input("age = ")
age_calc = (2024 - int(age_int))
print(age_calc)
print(f"OMG, you are {age_int} years old so you were born in {age_calc}")

# How to structure an f-string
score = 16

max_score = 26

score_as_decimal = score / max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
new_score = f'You scored {score_as_decimal}'
print(new_score)

```


# JSON !
[understanding_JSON](..%2Funderstanding_JSON)

**What does it stand for?**

- Javascript Object Notation.

**What is it used for?**

- Storing and exchanging data between systems.

**What is it written in?**

- It was developed for Javascript but it is a language-independent data format.

**Include a simple example of JSON:**
```json
{
  "name": "Alice",
  "age": 30,
  "city": "Wonderland",
  "is_student": true
}
```
**Advantages of using it?**

**Compact and Efficient Format:**

- JSON’s concise syntax allows for easy parsing of data.
- Its lightweight nature makes it efficient for transmitting data over networks.
APIs, web services, and microservices often use JSON due to its efficiency.

**Human-Readable:**

- JSON is both human-readable and machine-readable.
- Its simple text-based structure makes it easy for developers to read and write.
- Unlike more verbose formats (such as XML), JSON is straightforward to interpret.

**Widely Supported:**

- JSON is supported by virtually all major programming languages.
- Whether you’re using JavaScript, Python, PHP, Ruby, or others, JSON is a common choice.
- This widespread support makes it an ideal format for exchanging data between systems.

**Data Preservation:**

- JSON can represent complex data structures, including nested objects and arrays.
- When transmitted, object hierarchies and relationships are preserved.
- The receiving end can reassemble the data appropriately for its programming environment.

**Web Applications Prefer JSON Over XML:**

- JSON has largely replaced XML for web applications.
- It’s faster to parse and easier to work with.
APIs and RESTful services commonly use JSON for data exchange.



**What data types can it store/use?**

- It can use strings, arrays, booleans, numbers, objects and null data type

**What is the JSON syntax for:**

***Name value pairs?***

 - Name-Value Pair Syntax:
In JSON, a name-value pair consists of a field name (or key) followed by a colon (:) and then a value.
The field name (key) must be enclosed in double quotes (").
The value can be a string, number, boolean, object, array, or null.

***Objects?***
- A JSON object is enclosed in curly braces {}

***How to separate data (key/value pairs) from one another?***

- With a colon between the key and the value, then a comma between the key-value pairs

***JSON arrays (these are like lists in python)?***
```json
{
  "fruits": ["apple", "banana", "orange"]
}
```