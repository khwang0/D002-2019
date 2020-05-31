
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

print('Welcome to the rock-paper-scissor game!\nYou are going to play against the king!')
win = 0
# ascii art from https://www.asciiart.eu/people/body-parts/hand-gestures
while win < 3:
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
    p_choice = int(input())

# step2: generate a random choice for minion, save it in variable m_choice
    m_choice = random.randint(1, 3)



# status is used for the win/lose/draw of the game
# status = 1 means player wins; status = 2 means minion wins; status = 3 means draw;
# status = 4 means user gives invalid input, e.g. player inputs -1 or 4
    status = 0 # initialized as 0
# step 3: given choices from player and minion, decide the game status
    if(p_choice > 3 or p_choice < 1):
        status = 4
    else:
        status = (p_choice - m_choice) % 3
    if(status == 0):
        status = 3








# step4: display the minion's choice
    if status < 4:
        if m_choice == 1:
            print("King chooses rock!")
        elif m_choice == 2:
            print("King chooses paper!")
        elif m_choice == 3:
            print("King chooses scissor!")
    if status == 1:
        win += 1
        print("You win!")
        print("You are on a %d-game win streak." % win)
    elif status == 2:
        win = 0
        print("You lose!")
        print("Your win streak has been reset.")
    elif status == 3:
        print("Draw!")
    else:
        print("Wrong input.")
print("Congratulation! You overthrow the King!")    
