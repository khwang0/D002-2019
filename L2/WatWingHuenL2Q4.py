a = 1
c=a+1
d=a+2
y=0

while a<61:
    
    b=60-a-c-d
    x=int(a*b+b*c+c*d)
    print(a,b,c,d)
    if x<y:
        break
     
        
    elif x>y:
           y=x
           a=a+1
           c=c+1
           d=d+1
           print(x)
           
