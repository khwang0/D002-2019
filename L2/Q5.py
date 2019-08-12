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
while True:
    count = 0
    while count < 3:

            
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
        p_choice = input ("Your choice: \n")
        p_choice = int(p_choice)
# step2: generate a random choice for minion, save it in variable m_choice
        m_choice = random.randint(1,3)
        m_choice = int(m_choice)
# status is used for the win/lose/draw of the game
# status = 1 means player wins; status = 2 means minion wins; status = 3 means draw;
# status = 4 means user gives invalid input, e.g. player inputs -1 or 4
        status = 0 # initialized as 0
# step 3: given choices from player and minion, decide the game status

        number= p_choice - m_choice
        if p_choice > 3 or p_choice < 1:
            status=4
        elif number == 1 or number == -2:
            status=1
        elif number == -1 or number == 2:
            status=2
        elif number == 0:
            status=3

# step4: display the minion's choice
        if m_choice == 1:
            print("Minion chooses rock!")
        elif m_choice == 2:
            print("Minion chooses paper!")
        elif m_choice == 3:
            print("Minion chooses scissor!")

        if status == 4:
            print("Invalid input")
            continue
        if status ==3:
            print("Draw!")
            continue
        if status == 1:
            count = count + 1
            print("You win this round. You have to win %d more times." % (3-count))
        if status == 2:
            print("You lost. Try again.")
            break   
    if count == 3:
        break
print("You beat the king!")
