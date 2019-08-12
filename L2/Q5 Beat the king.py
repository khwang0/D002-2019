import random
print("Welcome to rock, paper and scissors: beat the king variant! You will need to beat the king three times in a row in order to win")
choice = int(input("input 1 for rock, 2 for paper or 3 for scissors:"))
M_choice = random.randint(1,3)
if(M_choice == 1):
    print("Minion chooses rock")
if(M_choice == 2):
    print("Minion chooses paper")
if(M_choice == 3):
    print("Minion chooses scissors")
if((choice == 1 and M_choice == 3) or (choice == 2 and M_choice == 1) or (choice == 3 and M_choice == 2)):
    print("You win! The usurper is rising")
    choose = int(input("Go again! input 1 for rock, 2 for paper or 3 for scissors:"))
    C_choice = random.randint(1,3)
    if(C_choice == 1):
        print("Minion chooses rock")
    if(C_choice == 2):
        print("Minion chooses paper")
    if(C_choice == 3):
        print("Minion chooses scissors")
    if((choose == 1 and C_choice == 3) or (choose == 2 and C_choice == 1) or (choose == 3 and C_choice == 2)):
        print("You win! The usurper is rising")
        z = int(input("Nearly there! input 1 for rock, 2 for paper or 3 for scissors:"))
        z = random.randint(1,3)
        if(y == 1):
            print("Minion chooses rock")
        if(y == 2):
            print("Minion chooses paper")
        if(y == 3):
            print("Minion chooses scissors")
        if((z == 1 and y == 3) or (z == 2 and y == 1) or (z == 3 and y == 2)):
            print("You win! The usurper becomes king")
        if((z == 1 and y ==2) or (z == 2 and y == 3) or (z == 3 and y == 1)):
           print("You Lose! The king keeps his throne")
        if((z == 1 and y == 1) or (z == 2 and y ==2) or (z == 3 and y == 3)):
            print("It's a draw! The king keeps his throne")
    if((choose == 1 and C_choice ==2) or (choose == 2 and C_choice == 3) or (choose == 3 and C_choice == 1)):
       print("You Lose! The king keeps his throne")
    if((choose == 1 and C_choice == 1) or (choose == 2 and M_choice ==2) or (choose == 3 and C_choice == 3)):
        print("It's a draw! The king keeps his throne")
if((choice == 1 and M_choice ==2) or (choice == 2 and M_choice == 3) or (choice == 3 and M_choice == 1)):
    print("You Lose! The king keeps his throne")
if((choice == 1 and M_choice == 1) or (choice == 2 and M_choice ==2) or (choice == 3 and M_choice == 3)):
    print("It's a draw! The king keeps his throne")
    
