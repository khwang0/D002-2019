def overlap(a1x,a1y,c1x,c1y,a2x,a2y,c2x,c2y):
    if c1x > a2x and c1y > a2y:
        return True
    else:
        return False

print(overlap(1,1,2,2,1.5,1.5,2.5,2.5)) #True
print(overlap(1,1,2,2,1.5,2.5,3,3))  #False  
print(overlap(1,1,2,2,1.5,1.5,1.75,3))   #True
      
