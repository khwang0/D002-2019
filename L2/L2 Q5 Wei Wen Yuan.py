import random
print("Can't get minion jpegs to load")
print("Welcome to rock, paper, and scissors!\nYou are going to play against a minion")
print("""


    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)

""")

choice= int(input("input 1 for rock, 2 for paper or 3 for scissors:\n"))
M_choice = random.randint(1,3)
if(M_choice == 1):
    print("Minion chooses rock")
if(M_choice == 2):
    print("Minion chooses paper")
if(M_choice == 3):
    print("Minion chooses scissors")
if((choice == 1 and M_choice == 3) or (choice == 2 and M_choice == 1) or (choice == 3 and M_choice == 2)):
    print("You win! Minion loses")
if((choice == 1 and M_choice ==2) or (choice == 2 and M_choice == 3) or (choice == 3 and M_choice == 1)):
    print("You Lose! Minion wins")
if((choice == 1 and M_choice == 1) or (choice == 2 and M_choice ==2) or (choice == 3 and M_choice == 3)):
    print("It's a draw! Play again!")
    
