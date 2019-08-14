tyui=0
for a in range(1,57):
    la=60-a
    for b in range(1,la-1):
        lb=la-b
        for c in range(1,lb-1):
            d=lb-c
            qwer=(a*b)+(b*c)+(c*d)
            if qwer>tyui:
                tyui=qwer
                q=a
                w=b
                e=c
                r=d
            print(str(a)+'  |  '+str(b)+'  |  '+str(c)+'  |  '+str(d)+'  |  '+str(qwer)+'  |  '+str(tyui))
print('a= '+str(q)+'  |  b= '+str(w)+'  |  c= '+str(e)+'  |  d= '+str(r))
