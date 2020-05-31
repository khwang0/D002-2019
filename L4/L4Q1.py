# Q1

# a) Gotcha.
# You are a Pokemon trainer and you catch new monster everyday.
# A list, which is called "collection", stores all kinds of pokemon that you
# have collected so far. The list "collection" does not stores how many same kind of
# monster you have got. Each monster of the same kind will be stored once.

collection = ["Pikachu", "Bulbasaur", "Squirtle", "Nidoqueen"]
newly_caught = ["Bulbasaur", "Kakuna", "Arbok", "Jigglypuff"]
for i in newly_caught:
    if i not in collection : # your code here
        collection += [i]        # your code here
print(collection) # should print ['Pikachu', 'Bulbasaur', 'Squirtle', 'Nidoqueen', 'Kakuna', 'Arbok', 'Jigglypuff']


# b) Shaking the stock market.
# You are given a list that stores the Hangseng Index
# of a period of time. Each number represents the HSI recorded at the end of a
# day. You want to find how many points it goes up and down in each day.
# Put those changes into another list.

hsi = [20000, 21000, 21500, 22125, 21015, 22013, 19942, 24500]
change = []
for i in range(7):
    change += [hsi[i+1]-hsi[i]]
print(change)  # should print [1000, 500, 625, -1110, 998, -2071, 4558]


# c) TV remote control
# Not sure how many of you are still watching TV. Assume we have a list of channels
# preset in your TV. If you press Up (U), it shows the next channel in the list.
# If you press Down (D), it shows the previous channel. If you press Off (O), the
# TV will explode and the program ends.

channels = ["TVB", "CCTV", "VIU", "RTHK", "Netflix", "TBS", "KBS"]
current_channel = 0
while True:
    print("You are now watching %s" % channels[current_channel])
    a = input("Please choose either Up/Down/Off\n")
    if a == 'U':
        current_channel = (current_channel + 1) % 7            
    if a == 'D':
        current_channel = (current_channel - 1) % 7
    if a == 'O':
        break
    # may be some more code

##
