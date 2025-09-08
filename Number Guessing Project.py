import art
import random
print(art.logo_guess)
game = "y"
def gameplay(live):
    while live > 0:
        print(f"You have {live} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < number:
            live -= 1
            print("Too low.")
            print("Guess again!")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            game == "n"
        else:
            live -= 1
            print("Too high.")
            print("Guess again!")

while game == "y":
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    number = random.randint(1,100)
    if diff == "easy":
        gameplay(10)
    elif diff == "hard":
        gameplay(5)
    game = input("Do you want to play again? Type 'y' for yes 'n' for no.").lower()
print("Goodbye!")


