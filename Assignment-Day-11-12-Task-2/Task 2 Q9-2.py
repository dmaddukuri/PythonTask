""" Read the two parts of the question below: 
 Write a program such that it asks users to “guess the lucky number”. 
 If the correct number is guessed the program stops, otherwise it continues forever. 
 Modify the program so that it asks users whether they want to guess again each time.
 Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. 
 The program stops if the user guesses the correct number or answers “no”. 
 ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
"""
number = 0

while True:
    number = int(input("guess the lucky number:"))
    answer = str(input("is this your lucky number ? yes or no "))
    if( answer == "yes"):
        break
    elif(answer == "no"):
        continue