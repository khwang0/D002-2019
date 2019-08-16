U = []
count = 0
for i in range(20):
    U += [i+1]
for a in range(16):
    for b in range(a+1, 17):
        for c in range(b+1, 18):
            for d in range(c+1, 19):
                for e in range(d+1, 20):
                    s = [U[a], U[b], U[c], U[d], U[e]]
                    t = []
                    p = True
                    for i in range(4):
                        t += [s[i+1] - s[i]]
                    for i in range(4):
                        if t[i] == 1:
                            p = False
                    if p:
                        count += 1
print('There are %d combinations' % count)
