a=0
max=0

for a in range(0,61):
    for b in range(0,60-a+1):
         for c in range(0,60-a-b+1):
             d=20-b-a-c
             value=a*b+b*c+c*d
             if value>max:
                 max=value

print(max)    
      
