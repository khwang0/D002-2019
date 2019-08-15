#ow----
#col|||||
now=[0,0,0,0,0,0,0,0,0]
win=0
def tnow():
    nowt1=str(now[0:3])
    nowt2=str(now[3:6])
    nowt3=str(now[6:9])
    print(nowt1)
    print(nowt2)
    print(nowt3)
tnow()
print('1 for P1\n2 for P2')
win=0
def p1():
    colc1 = int(input("P1\nPlease enter column"))
    rowc1 = int(input("P1\nPlease enter row"))
    if now[(colc1-1)*3+(rowc1-1)]!=0:
        print("It is taken already")
        p1()
    now[(colc1-1)*3+(rowc1-1)]=1
    tnow()
def p2():
    colc2 = int(input("P2\nPlease enter column"))
    rowc2 = int(input("P2\nPlease enter row"))
    if now[(colc2-1)*3+(rowc2-1)]!=0:
        print("It is taken already")
        p2()
    now[(colc2-1)*3+(rowc2-1)]=2
    tnow()
def check():
    if (now[0]==1 and now[1]==1 and now[2]==1) or (now[3]==1 and now[4]==1 and now[5]==1) or (now[6]==1 and now[7]==1 and now[8]==1) or  (now[0]==1 and now[3]==1 and now[6]==1) or (now[1]==1 and now[4]==1 and now[7]==1) or (now[2]==1 and now[5]==1 and now[8]==1) :
        win=1
    if  (now[0]==1 and now[4]==1 and now[8]==1) or  (now[2]==1 and now[4]==1 and now[6]==1) :
        win=1
    if (now[0]==2 and now[1]==2 and now[2]==2) or (now[3]==2 and now[4]==2 and now[5]==2) or (now[6]==2 and now[7]==2 and now[8]==2) or  (now[0]==2 and now[3]==2 and now[6]==2) or (now[1]==2 and now[4]==2 and now[7]==2) or (now[2]==2 and now[5]==2 and now[8]==2) :
        win=2
    if  (now[0]==2 and now[4]==2 and now[8]==2) or  (now[2]==2 and now[4]==2 and now[6]==2) :
        win=2
    if now[0]!=0 and now[1]!=0 and now[2]!=0 and now[3]!=0 and now[4]!=0 and now[5]!=0 and now[6]!=0 and now[7]!=0 and now[8]!=0 :
        win=3
def play():
    while win==0:
        p1()
        check()
        print(win)
        p2()
        check()
        print(win)
    if win==1:
        print('P1 WIN!')
    if win==2:
        print('P1 WIN!')
    if win==3:
        print('________Draw_________')
        replay=input('replay?')
        if replay=='yes':
            play()
play()
    









