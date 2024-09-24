# Use your code from the "Task: Get name, age and DOB details from a user".
# Mix the name, age and DOB into one list user_details_list
user_details_list = ["Ilhaan", 25, "14.03.1999"]
print(user_details_list)
print(type(user_details_list[1]))

# Print the user's name, age and DOB from the list
print(user_details_list)
# Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
print(type(user_details_list[1]))
# Ask the user for their height in cm and save it to the variable height
height = input("Please enter your height in cm")
print(height)
# Save height as a float in the list, and print the height from the list.
float_height = float(height)
user_details_list.append(float_height)
print(user_details_list)