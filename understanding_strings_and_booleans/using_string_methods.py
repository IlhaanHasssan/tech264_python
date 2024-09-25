str_with_extra_spaces = "   extra spaces at the start and end   "
#this is a variable which holds a string
print(len(str_with_extra_spaces))
#this prints the length of the string
print(str_with_extra_spaces)
# the strip method removes whitespaces in python
print(len(str_with_extra_spaces.strip()))
print(str_with_extra_spaces.strip())



example_text = "here's some text with some words of text"

# count how many times the substring 'text' occurs within example_text & print it to the screen
print(example_text.count("text"))
#count method tells you how many times a particular word occurs in a string

# convert example_text to lowercase & print it to the screen
print(example_text.lower())

# convert example_text to uppercase & print it to the screen
print(example_text.upper())

# capitalise the first letter in example_text & print it to the screen
print(example_text.capitalize())

# replace the word 'with' in example_text with a comma (,) instead & print it to the screen
new_example = example_text.replace("with", ",")
print(new_example)



