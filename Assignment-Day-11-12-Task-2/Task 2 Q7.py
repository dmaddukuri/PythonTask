""" Write a program that prints all the numbers from 0 to 6 except 3 and 6.
       Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement """

i=-1
while i < 6:
    i += 1    
    if i != 3 and i != 6:
        print(i)
        continue
    

