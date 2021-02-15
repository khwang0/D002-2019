def printer(secret, opened):
    i = 0

    while i < len(secret):
        if i in opened:
               print(secret[i], end = "")
        else:
            print("_", end="")
                
               
      
        
        
        
         
        i = i + 1
    print()
 #   return 

printer("apple", [1, 2])
printer("orange",[0,5])
printer("cat",[])
