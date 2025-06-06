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

rps = [rock, paper, scissors]
try:
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))
    if player not in [0, 1, 2]:
        print("Invalid choice! Please choose 0, 1, or 2.")
        exit()
except ValueError:
    print("Please enter a valid number!")

computer = random.randint(0,2)

print(rps[player])
print("Computer chose:")
print(rps[computer])

if player == computer:
    print("Draw")
elif player == 0 and computer == 2:
    print("You win")
elif player == 1 and computer == 0:
    print("You win")
elif player == 2 and computer == 1:
    print("You win")
else:
    print("You lose")