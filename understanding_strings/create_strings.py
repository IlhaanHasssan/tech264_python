#bad_string = 'I said 'Wow!''
#print(bad_string)

#Explain: Why does this fail?
#this string fails because the there are two sets of single quotes

#Find 3 ways to make this string assignment work
bad_string = 'I said "Wow!"'
print(bad_string)

bad_string_two ="I said 'Wow!'"
print(bad_string_two)

bad_string_three = '''I said "Wow!"'''
print(bad_string_three)


#Condition: The Wow! must be surrounded in quotes when it prints to the screen
#Explain: What is best practice when deciding what quotes to use around strings in Python?
#best practice = single quotes are generally easier to read, but if a string contains single-quote
#characters then double-quotes are better than escaping the single-quote characters
#generally best to avoid triple quotes of the same quote character because it can get confusing very quickly
#and very hard to read
