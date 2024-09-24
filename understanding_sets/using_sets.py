# Explain 2 main ways that sets are different to lists and tuples
#sets cannot have multiple occurrences of the same element & store unordered values

# Create a set named 'fruits' containing "apple", "banana", and "cherry"
fruits = {
    "apple",
    "banana",
    "cherry"
}

# Print the set 'fruits'
print('fruits:', fruits)

# Add "orange" to the fruits set using one of the set's methods.
fruits.add("orange")

# Print the set 'fruits' - check it's added
print('Updated fruits:', fruits)

# Remove "banana" from the fruits set using one of the set's methods.
fruits.remove("banana")
# Print the set 'fruits' - check it's removed
print('Removed banana:', fruits)
# Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
fruits.add("apple")
print('duplicate apple:', fruits)
#this doesn't work because sets don't accept multiple occurrences of the same element

# Print the final fruits set.
print('final fruit set:', fruits)
# Print the 2nd item in the set. If there is any problem doing this, explain.
# set elements are not indexed so you cannot access the second item in the set since it doesn't exist

