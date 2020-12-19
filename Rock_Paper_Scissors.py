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

signs = [rock,paper,scissors]

player_sign = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Invalid input
if player_sign >2 or player_sign < 0:
  print("You type invalid number, you lose!")
else:
  computer_sign = random.randint(0,2)

  print(signs[player_sign]+"\n"+"Computer chose:\n"+signs[computer_sign]+"\n")

  # Conditions
  #   Rock wins against scissors.
  #   Scissors win against paper.
  #   Paper wins against rock.

  if player_sign == computer_sign:
    print("It's a draw")

  elif ((player_sign == 0 and computer_sign == 2) or (player_sign == 2 and computer_sign == 1) or (player_sign == 1 and computer_sign == 0) ):
    print("You win")

  else:
    print("You lose")