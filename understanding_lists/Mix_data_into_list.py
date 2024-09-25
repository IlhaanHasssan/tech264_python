from understanding_variables_and_datatypes.get_name_age_DOB import name, age, DOB
#import get_name_age_DOB
# Use your code from the "Task: Get name, age and DOB details from a user".
# Mix the name, age and DOB into one list user_details_list
user_details_list = [name, age, DOB]

# Print the user's name, age and DOB from the list
print(user_details_list)

# Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
print(type(user_details_list[1]))
age_integer_type_change = int(user_details_list[1])
print(type(age_integer_type_change))

# Ask the user for their height in cm and save it to the variable height
height = input("Please enter your height in cm ")
print(f"You height is {height}cm")

# Save height as a float in the list, and print the height from the list.
float_height = float(height)
user_details_list.append(float_height)
print(user_details_list)