def printer(secret, opened):
    i = 0
    result = ""
    while i < len(secret):
         if i in opened:
             result = result + secret[i]
         else:
             result = result + "_"
         i=i+1
    print(result)
    
