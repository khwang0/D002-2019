# b) Shaking the stock market.
# You are given a list that stores the Hangseng Index
# of a period of time. Each number represents the HSI recorded at the end of a
# day. You want to find how many points it goes up and down in each day.
# Put those changes into another list.

hsi = [20000, 21000, 21500, 22125, 21015, 22013, 19942, 24500]
change = []

# your code here
for i in range(0,7):
    change.append(hsi[i+1]-hsi[i])

print(change)  # should print [1000, 500, 625, -1110, 998, -2071, 4558]


