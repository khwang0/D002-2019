channels = ["CCTVB", "CCTV", "VIU", "RTHK", "Netflix", "TBS", "KBS"]

current_channel = 0
while True:
    print("You are now watching %s" % channels[current_channel])
    a = input("Please choose either Up/Down/Off\n")
    if a == 'U':
        current_channel = (current_channel + 1)% len(channels)
    if a == 'D':
        current_channel = (current_channel - 1)%len(channels)
    if a == 'O':
        break
   
