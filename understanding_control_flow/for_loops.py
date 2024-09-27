# task 2: For Loops
#Follow the instructions below to create various 'for loops'.
#syntax and structure of a for loop:
# for item( refers to each element in your iterable, acts as your counter) in iterable(string, list, tuples, dictionaries, sets):
#      Body of the loop
#      Do something with 'item'

list_data = [1, 2, 3, 4, 5]

embedded_lists = [[1, 2, 3], [4, 5, 6]]

dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

#Looping through a list: for loops run through iterations a finite number of times
for num in list_data:
    double = num * 2
    print(f"{num} x 2 = {double}.")

#2. Loop through the 'embedded_lists' list
#Write another for loop to print the items inside of 'embedded_lists'. Each item in the list should be called 'data'
#It should output this to the screen:
#[1, 2, 3]
#[4, 5, 6]
for embedded_list in embedded_lists:
    print(f"list': {embedded_list}")

# 3. Loop through the lists embedded inside a list
# We need to access the data within the lists, so now we need an embedded loop. Create another loop inside the 'embedded_lists' for loop to list the individual items in the lists.
# You should end up with this output:
# [1, 2, 3]
# 1
# 2
# 3
# [4, 5, 6]
# 4
# 5
# 6
    for item in embedded_list:
        print(f"element': {item}")


# 4. Loop through the dictionary (dict_data) and print its keys
# Write another for loop to loop through the dictionary 'dict_data'. It should print the keys to the screen like this:
# 1
# 2
# 3
for key in dict_data:
    print(f"key: {key}")

# 5. Loop through the dictionary and print its values
# Write another for loop to loop through the dictionary 'dict_data'. Use to the dictionary's value() method to print the value for each key in the dictionary. Output should be:
# {'name': 'Bronson', 'money': '$0.05'}
# {'name': 'Masha', 'money': '$3.66'}
# {'name': 'Roscoe', 'money': '$1.14'}

for value in dict_data.values():
    print(f"value: {value}")

# 6. Loop to print the values of the dictionary items inside a dictionary
#Copy and paste the last for loop as a starting point for this loop. Generate an embedded for loop (a loop within a loop) to extract and print the values within the dictionary of each item in the dictionary. Output should be:
# Bronson
# $0.05
# Masha
# $3.66
# Roscoe
# $1.14
for value in dict_data.values():
    for sub_value in value.values():
        print(f"value of item: {sub_value}")

# 7. Loop to print specific values (money) of the dictionary items inside a dictionary
#Write another for loop to loop through the dictionary 'dict_data' but this time only print out the money values. Output should be:
# $0.05
# $3.66
# $1.14
for value in dict_data.values():
    print(f"money value: {value['money']}")

# 8. Loop through a list (list_data) with a nested if statement
#Write another loop to loop through the items in 'list_data' and include a nested (indented) if statement inside the loop so that when it loops it checks the number/item in list:
# if the number is less than 3, it prints 'less than 3'
# if the number equals 3, it prints 'I found three'
# if the number is greater than 3, it prints 'greater than 3'
# Output should be:
# less than 3
# less than 3
# I found three
# greater than 3
# greater than 3 
for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
        print("I found three")
    else:
        print("greater than 3")