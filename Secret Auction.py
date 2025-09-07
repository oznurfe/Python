import art
answer = "yes"
print(art.logo_calculator)
print("Welcome to the secret auction program.")
Secret_Auction = {}
while answer == "yes":
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))

    Secret_Auction[name] = bid
    answer = input("Are they any other bidders? Type 'yes' or 'no': ")
    print("\n" * 100)
print("\n" * 100)
winner = 0
winner_name = ""
for key in Secret_Auction:
    if winner < Secret_Auction[key]:
        winner = Secret_Auction[key]
        winner_name = key

print(f"The winner is {winner_name} with a bid ${winner}")



