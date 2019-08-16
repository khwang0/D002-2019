import random
switch = 0
nswitch = 0
for x in range(100):
        a = [0, 0, 0]
        a[random.randint(0, 2)] = 1
        choose = random.randint(0, 2)
        while True:
                b = random.randint(0, 2)
                if (b != choose and a[b] == 0):
                        break
        c = 3 - choose - b
        if a[c] == 1:
                switch += 1
        else:
                nswitch += 1
print('In 100 trials,')
print('Win after switching :', switch)
print('Loss after switching :', nswitch)
