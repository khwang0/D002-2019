
# Q1

# a) Gotcha.
# You are a Pokemon trainer and you catch new monster everyday.
# A list, which is called "collection", stores all kinds of pokemon that you
# have collected so far. The list "collection" does not stores how many same kind of
# monster you have got. Each monster of the same kind will be stored once.

collection = ["Pikachu", "Bulbasaur", "Squirtle", "Nidoqueen"]
newly_caught = ["Bulbasaur", "Kakuna", "Arbok", "Jigglypuff"]

for i in newly_caught:
    if i in collection : # your code here
        collection = collection + [i]   # your code here

print(collection) # should print ['Pikachu', 'Bulbasaur', 'Squirtle', 'Nidoqueen', 'Kakuna', 'Arbok', 'Jigglypuff']


# b) Shaking the stock market.
# You are given a list that stores the Hangseng Index
# of a period of time. Each number represents the HSI recorded at the end of a
# day. You want to find how many points it goes up and down in each day.
# Put those changes into another list.

hsi = [20000, 21000, 21500, 22125, 21015, 22013, 19942, 24500]
change = []
x = 1
while x < 8:
    change = change + [hsi[x]-hsi[x-1]]
    x= x+1
# your code here

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
        if current_channel == 6:
            current_channel = 0
        else:
            current_channel = current_channel + 1         # code
    if a == 'D':
        if current_channel == 0:
            current_channel = 6
        else:
            current_channel = current_channel - 1       # code
    if a == 'O':
        break
    # may be some more code



### Expected Result
##You are now watching TVB
##Please choose either Up/Down/Off
##U
##You are now watching CCTV
##Please choose either Up/Down/Off
##U
##You are now watching VIU
##Please choose either Up/Down/Off
##U
##You are now watching RTHK
##Please choose either Up/Down/Off
##D
##You are now watching VIU
##Please choose either Up/Down/Off
##D
##You are now watching CCTV
##Please choose either Up/Down/Off
##U
##You are now watching VIU
##Please choose either Up/Down/Off
##D
##You are now watching CCTV
##Please choose either Up/Down/Off
##D
##You are now watching TVB
##Please choose either Up/Down/Off
##D
##You are now watching KBS
##Please choose either Up/Down/Off
##D
##You are now watching TBS
##Please choose either Up/Down/Off
##U
##You are now watching KBS
##Please choose either Up/Down/Off
##U
##You are now watching TVB
##Please choose either Up/Down/Off
##O
##>>>
