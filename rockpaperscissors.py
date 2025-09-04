import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [paper, scissors, rock]
choice = int(input("For paper enter 0, for scissors enter 1 for rock enter 2: "))
cmp = random.randint(0,2)

if choice == 0:
    print("You:\n" + paper)
    if cmp == 0:
        print("Computer:\n" + paper)
        print("You both choose paper. Its draw!")
    elif cmp == 1:
        print("Computer:\n" + scissors)
        print("YOU LOST!")
    else:
        print("Computer:\n" + rock)
        print("YOU WIN!")
elif choice == 1:
    print("You:\n" + scissors)
    if cmp == 0:
        print("Computer:\n" + paper)
        print("YOU WIN!")
    elif cmp == 1:
        print("Computer:\n" + scissors)
        print("You both choose scissors. Its draw!")
    else:
        print("Computer:\n" + rock)
        print("YOU LOST!")
elif choice == 2:
    print("You:\n" + rock)
    if cmp == 0:
        print("Computer:\n" + paper)
        print("YOU LOST!")
    elif cmp == 1:
        print("Computer:\n" + scissors)
        print("YOU LOST!")
    else:
        print("Computer:\n" + rock)
        print("You both choose rock. Its draw!")
