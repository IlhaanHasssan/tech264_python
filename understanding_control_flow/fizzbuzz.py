# FizzBuzz Task
# Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz'
# multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'

for num in range(1, 101):  # print(f"number = {num}") #checking if num is printing 1-100
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(f"not fizz, buzz or fizzbuzz: {num}")


#If time: Improve the script so we can decide which numbers to substitute for "Fizz" and "Buzz"
#Refactor using functions:

def fizz_buzz(number, fizz_multiple = 3, buzz_multiple = 5):  # this function takes 3 arguments; number: the number we want to check
    #fizz_multiple: default value of 3 and buzz_multiple: default value of 5, there are the multiples for fizz and buzz
    result = ""  #initialise empty string called result
    if number % fizz_multiple == 0:
        result += "Fizz"
    if number % buzz_multiple == 0:
        result += "Buzz"
    return result or str(number)  #if neither conditions are met, result is returned with either fizz, buzz, both or original number as string

for num in range(1, 101):
    print(fizz_buzz(num, fizz_multiple=13, buzz_multiple=13))  # you can customize the multiples here

