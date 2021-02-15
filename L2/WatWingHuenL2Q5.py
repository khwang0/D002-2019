



import random

print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')

# ascii art from https://www.asciiart.eu/people/body-parts/hand-gestures

print("""
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
""")
player = int(input("Please input your choice\n"))
m_choice=random.randrange(1,3)






# step2: generate a random choice for minion, save it in variable m_choice




# status is used for the win/lose/draw of the game
# status = 1 means player wins; status = 2 means minion wins; status = 3 means draw;
# status = 4 means user gives invalid input, e.g. player inputs -1 or 4
# initialized as 0
# step 3: given choices from player and minion, decide the game status









# step4: display the minion's choice
if m_choice == 1:
    print("Minion chooses rock!")
elif m_choice == 2:
    print("Minion chooses paper!")
elif m_choice == 3:
    print("Minion chooses scissor!")

if m_choice == player:
    print("TRY AGAIN")
if m_choice == 1 and player==2:
    print("You Win")
if m_choice ==2 and player==3:
    print("You Win")
if m_choice ==3 and player==2:
    print("You Lose")
if m_choice ==2 and player==1:
    print("You Lose")


