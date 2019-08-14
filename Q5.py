am=0
while True:
    import random
    print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')
    print("""
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
""") 
    p=int(input("Please input your choice"))
    m=int(random.randint(1,3))
    status = -10
    if (p==1 and m==1) or (p==2 and m==2) or (p==3 and m==3):
        status=0
    if (p==1 and m==2) or (p==2 and m==3) or (p==3 and m==1):
        status=-1
    if (p==1 and m==3) or (p==2 and m==1) or (p==3 and m==2):
        status=1
# step4: display the minion's choice
    if m == 1:
        print("Minion chooses rock!")
    elif m== 2:
        print("Minion chooses paper!")
    elif m== 3:
        print("Minion chooses scissor!")
    if status==1 :
        print(' |||   U WIN   |||  ')
        am += 1
    if status==-1 :
        print(' |||   U LOSE   |||  ')
        am = 0
    if status==0 :
        print(' |||   DRAW   |||  ')
    if am==3:
        print('   |||||| SUCCESS ||||||   ')
        break
