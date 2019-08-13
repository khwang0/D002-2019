print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')
print("Please input your choice")
from random import randint
print("""
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
""")
p_choice = int(input("input your choice\n"))
m_choice = randint(1, 3)

status = 0
if p_choice == 1 and m_choice == 3:
    status = status+1
elif p_choice == 2 and m_choice == 1:
    status = status+1
elif p_choice == 3 and m_choice == 2:
    status = status+1
elif p_choice == 1 and m_choice == 2:
    status = status+2
elif p_choice == 2  and m_choice == 3:
    status = status+2
elif p_choice == 3 and m_choice == 1:
    status = status+2
elif p_choice == 1 and m_choice == 1:
    status = status+3
elif p_choice == 2 and m_choice == 2:
    status = status+3
elif p_choice == 3 and m_choice == 3:
    status = status+3
print(m_choice)
print(status)

#win = 0
if status == 1:
    print("You win!")
    #win = win + 1    
if status == 2:
    print("You lose!")
 #   win = 0
if status == 3:
    print("Draw!")
#print(win)
#if win = 3:
 #   print("Congradulations! You beat the king!")
