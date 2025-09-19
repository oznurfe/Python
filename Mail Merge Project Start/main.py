#TODO: Create a letter using starting_letter.txt
with open ("Input/Letters/starting_letter.txt", mode = "r") as letter:
    letter = letter.read()

letternames = []
with open("Input/Names/invited_names.txt", mode="r") as names:
    for name in names:
        letternames.append(name.strip())

for name in letternames:
    letter1 = letter.replace("[name]",name)
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as output:
        output.write(letter1)
