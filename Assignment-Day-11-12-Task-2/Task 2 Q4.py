"""Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”
"""
i=5
while i > 0:
    print(i)
    i = int(input("Enter the value for i variable: "))
    print(i)
    if i > 0:
        print("Going Good")
        continue
    if i < 0:
        print("It's Over")
        break