#what is slicing string?
#slicing allows you to extract a portion of the string by specifying a start and end index
#uses format string[start:end]
#The start index is where slicing begins (inclusive)
# the end index is where it ends (exclusive).

Hw= "Hello world"

# Find out how many characters Hw has
print(len(Hw))
#prints number of letters in Hw variable
#output = 11

# Get the character in the first position in Hw
print(Hw[0])
#uses the index of the first letter [0] to print the first letter

# Get the last character and 2nd last character
print(Hw[-1])
print(Hw[-2])
#uses negative index to find last  and second last characters

# Write a comment to EXPLAIN what does this do
print(Hw[2:])
#this slices the string from the 2nd index to the end of the string

# Write a comment to EXPLAIN what does this do
print(Hw[-3:])
#slices the string from the 3rd to last character to the end of the string

# Write a comment to EXPLAIN what does this do
print(Hw[:5])
# slices the string from the beginning to the 5th index ([5])

# Starts from the second, stops at the fifth (doesn't include it)
print(Hw[2:5])

