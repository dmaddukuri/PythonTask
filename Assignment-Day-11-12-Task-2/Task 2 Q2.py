""" Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition 
If User Enter 2 - Subtraction
If User Enter 3 - Division
If USer Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose an option 5.
At the end if the answer of any operation is Negative print a statement saying “zsa”
NOTE: At a time user can perform one action at a time. """


op = int(input("Enter 1 - Addition \nEnter 2 - Subtraction \nEnter 3 - Division \nEnter 4 - Multiplication \nEnter 5 - Average\n"))
if op < 5:
    first = int(input("Enter the value for first variable: "))
    second = int(input("Enter the value for second variable: "))
    if(op == 1):
        add = first + second
        if add > 0:
            print("Addition: ")
            print(add)
        else:
            print("zsa")
    if(op == 2):        
        sub = first - second
        if sub > 0:
            print("Subtraction: ")
            print(sub)
        else:
            print("zsa")
    if(op == 3):       
        div = first / second
        if div > 0:
            print("Division: ")
            print(div)
        else:
            print("zsa")
    if(op == 4):
        mul = first * second
        if mul > 0:
            print("Multiplication: ")
            print(mul)
        else:
            print("zsa")

elif op == 5:
    print ("enter two more numbers as first1 and second2 for calculating the average")
    first1 = int(input("Enter the value for first1 variable: "))
    second2 = int(input("Enter the value for second2 variable: "))
    avg = (first1 + second2) / 2
    if avg > 0:
            print("Average: ")
            print(avg)
    else:
        print("zsa")
elif op > 5:      
    print ("Wrong input, Please enter numbers (1-5)")

