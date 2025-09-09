import random
import art
import game_data

A = random.choice(game_data.data)
game_start = True
score = 0

def compare_to(first, second):
    if first > second:
        return "A"
    else:
        return "B"

def delete(score):
    if score != 0:
        print("\n" * 100)

while game_start == True:
    delete(score)
    B = random.choice(game_data.data)
    if A == B:
        B = random.choice(game_data.data)
    print(art.logo_hl)
    if score != 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}")
    print(art.vs)

    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if answer == compare_to(A["follower_count"], B["follower_count"]) :
        score += 1
        A = B
    else:
        print("\n" * 100)
        print(art.logo_hl)
        print(f"Sorry you're wrong' Your final score: {score}")
        game_start = False

