# Before finishing the game below, answer these questions:
#
# How are tuples similar to lists?
#tuples contain an ordered collection of items, that can contain different data types

# Are tuples immutable and what does this mean?
#yes, tuples are immutable meaning they cannot be changed once created

# What other data types are immutable?
#numbers, booleans and strings are also immutable

# What is a good use case for tuples?
#when your data shouldn't change such as coordinates

# What does the following piece of code do?

essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))

#this code shows a list of items then is uses the .count method to check how many times bread is in the list/tuple

# "Stranded on a Desert Island" game

# Rationale: Practice tuples

# Type of exercise: Finish the code

print("You are stranded on a desert island. You can take only THREE items.")

essential_item1 = input("What is an essential item you would take? ")

essential_item2 = input("What is an essential item you would take? ")

essential_item3 = input("What is an essential item you would take? ")

# save the items as a tuple

essentials_tuple = (essential_item1, essential_item2, essential_item3)


# print the tuple

print("Here are your items as a tuple:", essentials_tuple)

print("")

print("I lied. You can take one more item.")

essential_item4 = input("What is one more essential item you would take? ")

# try to add the 4th item to the tuple

# if you can't add the 4th item, work out how to save the 4th item to the tuple

essentials_tuple = (essential_item1, essential_item2, essential_item3, essential_item4)
# essentials_tuple = essentials_tuple + (essential_item4, )

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)

#you cant add items to s tuple with a method, you must include in the original tuple
#you can amend a list inside a tuple with .append method