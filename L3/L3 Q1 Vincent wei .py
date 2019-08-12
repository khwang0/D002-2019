from math import*
p = int(input("How many people are sharing the bill"))
b = float(input("How much is the bill?"))
print("Kevin paid the bill first. But Kevin only has 100 dollar notes")
x = ceil(b/100)*100
z = x - b
y = (x-z)/p
print("So Kevin is going to paid $%d." % (x)) 
print("The cafe returns %f of change to Kevin." % (z))
print("Each one should give %f to Kevin." % (y))


          
