def printer(sec,op):
    sec=list(sec)
    i=0
    re = list('_'*len(sec))
    for x in range(1,len(op)):
        re[ int(op[int(i)]) ]=sec[ int(op[int(i)]) ]
        i+=1
    re = ' '.join(re)
    print(re)
printer('apple',[1,2])
