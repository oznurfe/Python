import art
import random

def check_11(decks):
    total = sum(decks)
    while total > 21 and 11 in decks:
        decks.remove(11)
        decks.append(1)
        total = sum(decks)

cards = [11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10]
game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()

while game_start == "y":
    print(art.logo_blackjack)
    yours = []
    computers = []
    scorey = 0
    scorec = 0
    for i in range (0,2):
        yours.append(random.choice(cards))
        computers.append(random.choice(cards))

    print(f"Your cards: {yours} \nComputer's first card: {computers[0]}")
    another_card = input("Type 'y' to get another card, type 'n' to pass.").lower()

    while another_card == "y":
        yours.append(random.choice(cards))
        check_11(yours)
        scorey = sum(yours)
        if scorey < 21:
            print(f"Your cards: {yours}, current score: {scorey} \nComputer's first card: {computers[0]}")
            another_card = input("Type 'y' to get another card, type 'n' to pass").lower()
        else:
            another_card = "n"
    scorey = sum(yours)

    if scorey < 21:
        while sum(computers) < 17:
            computers.append(random.choice(cards))
            check_11(computers)
        scorec = sum(computers)
        print(f"Your cards: {yours}, final score: {scorey} \nComputer's final cards: {computers}, final score: {scorec}")
        if scorec > 21:
            print("You Win!")
        else:
            if scorey < scorec:
                print("You Lose!")
            elif scorey == scorec:
                print("Draw!")
            else:
                print("You Win!")

    elif scorey == 21:
        print(f"Your cards: {yours}, final score: {scorey} \nComputer's final cards: {computers}, final score: {scorec}")
        if len(yours) < len(computers):
            print("You Win!")
        elif len(yours) == len(computers):
            print("Draw!")
        else:
            print("You Lose!")

    else:
        print(f"Your cards: {yours}, final score: {scorey} \nComputer's final cards: {computers}, final score: {scorec}")
        print("You Lose!")

    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
print("Goodbye!")
