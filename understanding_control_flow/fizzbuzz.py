# FizzBuzz Task
# Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz'
# multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'

for num in range(1, 101): # print(f"number = {num}") #checking if num is printing 1-100
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)