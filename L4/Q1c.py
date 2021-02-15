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
        if current_channel > 6:
            current_channel = 0
            print("You are now watching %s" % channels[current_channel])
            a = input("Please choose either Up/Down/Off\n")
        else:
            current_channel = current_channel + 1
            print("You are now watching %s" % channels[current_channel])
            a = input("Please choose either Up/Down/Off\n")
    if a == 'D':
        if current_channel < 0:
            current_channel = 6
            print("You are now watching %s" % channels[current_channel])
            a = input("Please choose either Up/Down/Off\n")
        else:
            current_channel = current_channel - 1
            print("You are now watching %s" % channels[current_channel])
            a = input("Please choose either Up/Down/Off\n")
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
