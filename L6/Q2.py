win_tally_stick = 0
win_tally_change = 0
totalplays = 0
choice = 1
while choice <=3:
    car = 1
    while car <=3:
        if choice == car:
            win_tally_stick = win_tally_stick + 1
        if choice != car:
            win_tally_change = win_tally_change + 1
        totalplays = totalplays+1
        car = car + 1
    choice = choice + 1

print("Winrate for sticking to original choice: ", win_tally_stick/totalplays)
print("Winrate for changing the choice: ", win_tally_change/totalplays)
