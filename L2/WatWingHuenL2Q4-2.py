a=1
c=1
d=1
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

a=1
b=1
d=1
j=0

while c<61:
    
    c=60-b-a-d
    h=int(a*b+b*c+c*d)
    print(a,b,c,d)
    if h<j:
        break
     
        
    elif h>j:
           j=h
           b=b+1
           c=c+1
           d=d+1
           print(j)
if j>x:
    x=j



b=1
c=1
d=1
l=0

while b<61:
    
    a=60-b-c-d
    z=int(a*b+b*c+c*d)
    print(a,b,c,d)
    if z<l:
        break
     
        
    elif z>l:
           l=z
           b=b+1
           c=c+1
           d=d+1
           print(z)
if z>x:
    x=z

a=1
c=1
b=1
w=0

while d<61:
    
    d=60-b-c-a
    e=int(a*b+b*c+c*d)
    print(a,b,c,d)
    if e<w:
        break
     
        
    elif e>w:
           w=e
           b=b+1
           c=c+1
           a=a+1
           print(w)
if w>x:
    x=w
   
