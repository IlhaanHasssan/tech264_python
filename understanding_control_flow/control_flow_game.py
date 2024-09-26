# Battle game
#Make a 2 player battle game using Python.
#Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.
#If Player 2, let them pick the character/fighter they want. If CPU, assign a character/fighter randomly.
#The two Pokemon/fighters/characters need to fight.
#A winner must be declared via some sort of calculation.
#Bonus: Want to play again?
#Note: No Pygame or Turtle allowed. CLI only.

# Sample fighters (you can add more!)
import random

# Sample fighters (you can add more!)
fighters = {
    "Mewtwo": {"health": 100, "attack": 20},
    "Pikachu": {"health": 80, "attack": 25},
    "Charizard": {"health": 90, "attack": 22},
    "Venusaur": {"health": 110, "attack": 18},
    "Garchomp": {"health": 120, "attack": 15}
}

def choose_fighter(player_num):
    #Prompt player to choose a fighter or assign one randomly
    print(f"Player {player_num}, choose your fighter:")
    for i, fighter in enumerate(fighters.keys(), start=1):
        print(f"{i}. {fighter}")
    choice = input("Enter the number of your chosen fighter: ")
    return list(fighters.keys())[int(choice) - 1]

def battle(fighter1, fighter2):
    """Simulate the battle between two fighters."""
    while True:
        # Fighter 1 attacks Fighter 2
        damage = random.randint(1, fighters[fighter1]["attack"])
        fighters[fighter2]["health"] -= damage
        print(f"{fighter1} attacks {fighter2} for {damage} damage!")

        # Check if Fighter 2 is defeated
        if fighters[fighter2]["health"] <= 0:
            print(f"{fighter2} has been defeated!")
            return fighter1

        # Fighter 2 attacks Fighter 1
        damage = random.randint(1, fighters[fighter2]["attack"])
        fighters[fighter1]["health"] -= damage
        print(f"{fighter2} attacks {fighter1} for {damage} damage!")

        # Check if Fighter 1 is defeated
        if fighters[fighter1]["health"] <= 0:
            print(f"{fighter1} has been defeated!")
            return fighter2

def main():
    print("Welcome to the Battle Game!")
    player1 = choose_fighter(1)
    player2 = choose_fighter(2)

    winner = battle(player1, player2)
    print(f"\n{winner} wins the battle! 🎉")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("Thanks for playing! See you next time!")

if __name__ == "__main__":
    main()