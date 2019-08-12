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


# step2: generate a random choice for minion, save it in variable m_choice

counts=1


# status is used for the win/lose/draw of the game
# status = 1 means player wins; status = 2 means minion wins; status = 3 means draw;
# status = 4 means user gives invalid input, e.g. player inputs -1 or 4
status = 0 # initialized as 0
# step 3: given choices from player and minion, decide the game status


while counts < 4:
    m_choice=random.randint(1,3)
        
    p_choice=int(input("what is your choice"))
    if (p_choice==1 and m_choice==3) or(p_choice==2 and m_choice==1) or (p_choice==3 and m_choice==2):
        print ("you won",counts,"times")
        counts = counts + 1
        status = 1
    elif (p_choice==3 and m_choice==1) or (p_choice==1 and m_choice==2) or (p_choice==2 and m_choice==3):
        status = 2
        counts = counts + 0
        
    elif p_choice == m_choice:
        status = 3
        counts = counts + 0
        
    else:
        status = 4


    # step4: display the minion's choice
    if m_choice == 1:
        print("Minion chooses rock!")
    elif m_choice == 2:
        print("Minion chooses paper!")
    elif m_choice == 3:
        print("Minion chooses scissor!")

    if counts == 3:
        status = 1
        # ascii art from http://textart4u.blogspot.com/2013/08/minions-emoticons-text-art-for-facebook.html
    # step 5: display the final result with ascii art
    if status == 1:
        print("You Win! Minion Loses!")
        print("""
    ──────────▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ────────█═════════════════█
    ──────█═════════════════════█
    ─────█═══▄▄▄▄▄▄▄═══▄▄▄▄▄▄▄═══█
    ────█═══█████████═█████████═══█
    ────█══██▀────▀█████▀────▀██══█
    ───██████──█▀█──███──█▀█──██████
    ───██████──▀▀▀──███──▀▀▀──██████
    ────█══▀█▄────▄██─██▄────▄█▀══█
    ────█════▀█████▀───▀█████▀════█
    ────█═════════════════════════█
    ────█══════════▄▀▀▀▄══════════█
    ───▐▓▓▌═══════▀═════▀═══════▐▓▓▌
    ───▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌
    ───█══▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌══█
    ──█══▌═▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌═▐══█
    ──█══█═▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌═█══█
    ──█══█═▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌═█══█
    ──█══█═▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌═█══█
    ──█══█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█══█
    ─▄█══█▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█══█▄
    ─█████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─█████
    ─██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─██████
    ──▀█▀█──▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌───█▀█▀
    ─────────▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
    ──────────▐▓▓▓▓▌──▐▓▓▓▓▌
    ─────────▄████▀────▀████▄
    ─────────▀▀▀▀────────▀▀▀▀
        """)
    elif status == 2:
        print("You Lose! Minion Wins!")
        print("""
    ──────────▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ────────█═════════════════█
    ──────█═════════════════════█
    ─────█═══▄▄▄▄▄▄▄═══▄▄▄▄▄▄▄═══█
    ────█═══█████████═█████████═══█
    ────█══██▀────▀█████▀────▀██══█
    ───██████──█▀█──███──█▀█──██████
    ───██████──▀▀▀──███──▀▀▀──██████
    ────█══▀█▄────▄██─██▄────▄█▀══█
    ────█════▀█████▀───▀█████▀════█
    ────█═════════════════════════█
    ────█═════════▀▄═══▄▀═════════█
    ───▐▓▓▌═════════▀▀▀═════════▐▓▓▌
    ───▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌
    ───█══▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌══█
    ──█══▌═▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌═▐══█
    ──█══█═▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌═█══█
    ──█══█═▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌═█══█
    ──█══█═▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌═█══█
    ──█══█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█══█
    ─▄█══█▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█══█▄
    ─█████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─█████
    ─██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─██████
    ──▀█▀█──▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌───█▀█▀
    ─────────▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
    ──────────▐▓▓▓▓▌──▐▓▓▓▓▌
    ─────────▄████▀────▀████▄
    ─────────▀▀▀▀────────▀▀▀▀
    """)
    elif status == 3:
        print('Draw!')
        print("""
    ──────────▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ────────█═════════════════█
    ──────█═════════════════════█
    ─────█═══▄▄▄▄▄▄▄═══▄▄▄▄▄▄▄═══█
    ────█═══█████████═█████████═══█
    ────█══██▀────▀█████▀────▀██══█
    ───██████──█▀█──███──█▀█──██████
    ───██████──▀▀▀──███──▀▀▀──██████
    ────█══▀█▄────▄██─██▄────▄█▀══█
    ────█════▀█████▀───▀█████▀════█
    ────█═════════════════════════█
    ────█═══════▄▄▄▄▄▄▄▄▄▄▄═══════█
    ───▐▓▓▌═════════════════════▐▓▓▌
    ───▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌
    ───█══▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌══█
    ──█══▌═▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌═▐══█
    ──█══█═▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌═█══█
    ──█══█═▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌═█══█
    ──█══█═▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌═█══█
    ──█══█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█══█
    ─▄█══█▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█══█▄
    ─█████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─█████
    ─██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─██████
    ──▀█▀█──▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌───█▀█▀
    ─────────▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
    ──────────▐▓▓▓▓▌──▐▓▓▓▓▌
    ─────────▄████▀────▀████▄
    ─────────▀▀▀▀────────▀▀▀▀
    """)
    else:
        print("Wrong input!") # the unclear result should be due to the unexpected input



