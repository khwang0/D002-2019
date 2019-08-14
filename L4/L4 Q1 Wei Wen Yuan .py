# Q1

collection = ["Pikachu", "Bulbasaur", "Squirtle", "Nidoqueen"]
newly_caught = ["Bulbasaur", "Kakuna", "Arbok", "Jigglypuff"]

for i in newly_caught:
    if i not in collection:
        collection.append(i)
print(collection)

# Q2

hsi = [20000, 21000, 21500, 22125, 21015, 22013, 19942, 24500]
change = []
for i in range(0,7):
    change.append(hsi[i+1]-hsi[i])
print(change)

# Q3

channels = ["TVB", "CCTV", "VIU", "RTHK", "Netflix", "TBS", "KBS"]
channel = 0
while True:
    print("You are now watching %s" % channels[channel])
    a = input("Please choose either Up/Down/Off\n")
    if a == 'Up':  
        if channel < 6:
            channel = channel + 1
        else:
            channel = channel - 7 
    if a == 'Down':
        if channel > 0:
            channel = channel - 1
        else:
            channel = channel + 7
    if a == 'Off':
            print("Shutting off")
            break
