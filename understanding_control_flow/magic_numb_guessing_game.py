#Level 1
import random
#Challenge yourself to get Level 1 done in 15 min
#Comments in the code are to help you meet user requirements, but you may need to write code in the order you think is necessary
# Level 1: Guess the Magic Number
# User story 1: As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
# User story 2: As a user, I want to be able to guess a number and know if I need to go higher or lower.
# User story 3 : As a user, I don't want my guesses wasted if I enter something accidentally as my guess which are not digits.
# User story 4 : As a user, after each guess, I would like to know how many guesses I have left.
# User story 5 : As a user, I would like the magic to be randomly generated each time I play so it is more fun.
# User story 6 : As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly, and I've used up all my tries.
# Level 2 and 3: Random magic number and reveal at the end

magic_number = random.randint(1, 100)  # Generate a random magic number between 1 and 100
print(magic_number)
guesses_left = 5

while guesses_left > 0:
    guess = input("Guess the magic number (between 1 and 100): ")

    if not guess.isdigit() or int(guess) > 100:
        print("Please enter a valid number that is less than 100.")
        continue

    user_guess = int(guess) # can't enter a guess that isn't an int

    if user_guess == magic_number:
        print("Congratulations! You've guessed the magic number!")
        break
    elif user_guess < magic_number:
        print("Aim higher!")
    else:
        print("Aim lower!")

    guesses_left -= 1
    print(f"Guesses left: {guesses_left}")

if guesses_left == 0:
    print(f"Game over, the magic number was {magic_number}. Try harder next time!")

