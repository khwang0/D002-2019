# L2 Worksheet

1.  Ask the user to input an positive integer
and determine if it is a prime number. Save the file as `Q1.py`

2. Study the program below. Write down the output of the program when the user input 10.
```py
n = int(input("Please input an positive integer number:\n"))
y = 2
while y < n:
    y = y + 1
    if y % 2 == 0:
        print("%d is even continue" % y)
        continue
    x = int(y/2)
    while x > 1:
        if y % x == 0:
            print("%d has factor %d; break" % (y, x))
            break
            x = x - 1
    if x == 1:
        print("%d is a prime" % y)
            

```
Save the file as `Q2.py` (Note: the result itself are not python code, you should write 
them as a comment like 
```
'''Please input an positive integer number:  '''
'''3 is prime'''
'''4 has factor 2'''
'''break'''
....
```

3. Starts with the following code, write a program that prints the largest number found in the sequence. Save the file as `Q3.py`
```
for n in [-120, 14, 93, 320, 1, -999]
```

4. Solve a math problem: given `a`, `b`, `c`, `d` are positive integers and `a + b + c + d = 60`. Find the maximum value of `ab + bc + cd` using loop. Save the file as `Q4.py`

5. Using the skeleton code [Q5.py](Q5.py) to complete the Paper-Rock-Scissor game. Save the file as `Q5.py`

6. Using the skeleton code [Q6.py](Q6.py) to complete the number guessing game. Save the file as `Q6.py`

7. (Bonus) Extend the code you have written in Q6 to make it a 2-players game. Show us your work and no need to submit it. The program will ask player 1 to input its guess by printing:
> Player 1 input your guess: 

	If player 1 guess it right, the game stops and declare player 1 wins. Otherwise it switches to player 2 until either one of the players win (instead of 3 chances).

