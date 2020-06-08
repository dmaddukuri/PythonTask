# 1.	Write a program in Python to perform the following operation:
    #If a number is divisible by 3 it should print “Consultadd” as a string
    #If a number is divisible by 5 it should print “c” as a string
    #If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.

x = int(input("Enter the value: "))

if (x % 3)==0:
    print("Consultadd")
if (x % 5)==0:
    print("c")
if (x % 3)==0 and (x % 5)==0:
    print("Consultadd Python Training")

