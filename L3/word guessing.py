import random

np = int(input("1 player or 2 players?\n"))

if np == 1:
    sample = ["apple", "mango", "peach", "lemon", "grape", "melon"]
    word = random.choice(sample)


if np ==2:
    word = input("Please eneter a word\n")


a = ["-"]*len(word)
display = ''.join(a)
w = list(word)
dis = list(display)
c = 0
life = 3

print ("You have 3 lives for errors. Game start!\n")

while c< len(w) and life>0 :
    print (display)
    p_choice = input("Please guess a letter\n")
    if p_choice in w:
        dis[w.index(p_choice)] = w[w.index(p_choice)] 
        display = ''.join(dis)
        w[w.index(p_choice)] = '/'
        c = c+1
    else:
        life = life - 1
        print("Nope.. Try again. You got %d lives left..."%life)




if c == len(w):
    print ("You guessed it! It's", word)

if life == 0:
    print ("Oops... You died...")


        
        
