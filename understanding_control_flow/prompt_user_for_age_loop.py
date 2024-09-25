#1. Loop until age is all digits
#Look at this code:
# Ask user for their age
age = input("What is your age? ")

print(f" Your age is {age}")

#The problem with this code is that even if the user is 20, they could enter "20" or "twenty". Let's standardise the input to get the age as digits...
user_prompt = True
while user_prompt:
    age = input("What is your age? ")

    if age.isdigit() and int(age) <= 117:  #output won't work unless age is converted to int as math operators don't work on strings
        user_prompt = False
    else:
        print("Please enter your age using digits(up to 117 years old)!")

print(f"your age is {age}")

# 2. Also check age is in the correct range
# Our code now works to stop our user from inputting strings, floats, and negative numbers, but at the moment the user could say they are 356000 years old if they want.
# Assuming the oldest person alive today is 117, modify your code to only allow a maximum of 117 as the age.
# Hint: You already have an 'if statement' to check 'age' is all digits. Use the 'and' keyword to ALSO check 'age' is not too high.

