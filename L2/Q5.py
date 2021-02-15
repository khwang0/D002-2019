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
win = 0

v = (p_choice - m_choice + 3) %3
if v == 0:
    print("tie")
    win = win + 1
if v == 1:
    print("Player wins")
    win = win + 1
if v == 2:
    print("Player lose")
    win = win + 1
    
print("Dave's choice is %d." % m_choice)




if win == 3:
    print("Congradulations! You beat the king!")
