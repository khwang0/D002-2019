hsi = [20000, 21000, 21500, 22125, 21015, 22013, 19942, 24500]
change = []
i = 0
for i in range(0, 7):
    change.append(hsi[i+1] - hsi[i])

print(change)
