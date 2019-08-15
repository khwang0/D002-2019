# L2 Q5: play rock-paper-scissor - Beat the King
# You need to win the king three times in a row in order to throw him away from his throne
# Carefully think about where a loop should be place
# Suggested Logic:
#
# Repeat the following until you really win
#        Challenge the king three times, in each challenge
#               pick a choice for the King and a choice for the player
#               Repeat this if it is draw
#                      pick a choice for the King and a choice for the player
#               if fail the challenge, break from this loop
#        




# Import necessary modules
import random

print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')

# ascii art from https://www.asciiart.eu/people/body-parts/hand-gestures
print("Please input your choice")
print("""
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
""") # 1 for rock; 2 for paper; 3 for scissor

# step1: get player's choice, save it in variable p_choice
p_choice = int(input("Please enter 1-3: "))

# step2: generate a random choice for minion, save it in variable m_choice
from random import randint
m_choice = randint(1,3)



# status is used for the win/lose/draw of the game
# status = 1 means player wins; status = 2 means minion wins; status = 3 means draw;
# status = 4 means user gives invalid input, e.g. player inputs -1 or 4
status = 0 # initialized as 0
# step 3: given choices from player and minion, decide the game status

if (p_choice < 1 or p_choice > 3):
    status = 4

d = (m_choice - p_choice) % 3
if d == 0:
    status = 0
if d == 1:
    status = 2
if d == 2:
    status = 1




# step4: display the minion's choice
if m_choice == 1:
    print("Minion chooses rock!")
elif m_choice == 2:
    print("Minion chooses paper!")
elif m_choice == 3:
    print("Minion chooses scissor!")
