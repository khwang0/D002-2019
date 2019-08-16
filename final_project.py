##########Q1
temp=[]
import math
ans=[math.inf,None,None]
for i in range(1,11):
    temp.append(int(input('please input the %d st/nd/rd/th number' %i)))
temp.sort()
n=0
while True:
    if temp[n+1]-temp[n] < ans[0]:
         ans[0]=temp[n+1]-temp[n]
         ans[1]=temp[n+1]
         ans[2]=temp[n]
    n+=1
    if n==9:
        break
print('the neaerest numbers are ' +str(ans[1]) +' and ' + str(ans[2]))
print('their difference is %d'%ans[0])
##########Q2
door=['car','goat','goat']
cT=0
cF=0
import random
def change():
    global cT
    choice=random.randint(1,3)
    if choice==2:
        print('Door 3 is opened!')
    else :
        print('Door 2 is opened!')
    if choice== 2 or choice==3:
        cT+=1
def changeF():
    global cF
    choice=random.randint(1,3)
    if choice==2:
        print('Door 3 is opened!')
    else :
        print('Door 2 is opened!')
    if choice==1:
        cF+=1
for i in range(0,1000):
    change()
    changeF()
print('the chance for change is %d / 1000'%cT)
print('the chance for unchange is %d / 1000'%cF)
if cT>cF :
    print('chance for change is better')
if cF>cT:
    print('chance for unchange is better')
else :
    print('their chances are the same')
##########Q3
ans=[]
x=0
for q in range(1,21):
    for w in range(1,21):
        for e in range(1,21):
            for r in range(1,21):
                for t in range(1,21):
                    a=[q,w,e,r,t]
                    a.sort()
                    x+=1
                    if a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[4] :
                        continue
                    if a[1]-a[0]==1 or a[2]-a[1]==1 or a[3]-a[2]==1 or a[4]-a[3]==1 :
                        continue
                    if (a in ans) == True :
                        continue
                    ans.append(a)
print('the number of combination is '+str(len(ans)))

        
