print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')
print("Please input your choice")
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
m_choice = range(0,3)

status = 0
if p_choice == 1 and m_choice == 3:
    status = status + 1
elif p_choice == 2 and m_choice ==1:
    status = status + 1
elif p_choice == 3 and m_choice == 2:
    status = status + 1
elif p_choice == 1 and m_choice == 2:
    status = status + 2
elif p_choice == 2  and m_choice == 3:
    status = status + 2
elif p_choice == 3 and m_ choice == 1:
    status = status + 2
elif p_ choice == 1 and m_choice == 1:
    status = status + 3
elif p_choice == 2 and m_choice == 2:
    status = status + 3
elif p_choice == 3 amd m_choice == 3:
    status = status + 3

