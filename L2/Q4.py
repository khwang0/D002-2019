
sum = int(input("a+b+c+d = ?\n") )
a = int(sum/4)
num = [a,a,a,a]
mmp = 0

print("Possible combinations:")
for x in range (0,3):
      y = 15 + x*14 
      for num[x] in range (y, 0, -1):

        arr = list(num)
        arr.sort()

        mp = arr[0]*arr[2]+arr[2]*arr[3]+arr[3]*arr[1]

        if mp> mmp:
           mmp = mp
           v = list(arr)

        print("a=%d b=%d c=%d d=%d" % (arr[0], arr[2], arr[3], arr[1]))
        num[x+1] = num[x+1] +1
        
print("Maximum value of ab+bc+cd =", mmp)
print("a=%d b=%d c=%d d=%d" % (v[0], v[2], v[3], v[1]))



