""" Write a program in Python to complete the following task:
Create two different list as in even_list and odd_list
Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
Keep that in mind you can only add 5 items in each list
Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list. """


even_list1 = [] 
odd_list1 = [] 

for i in range(5):
    x=int(input("enter a number range(1,50):"))
    if(x%2==0):
        even_list1.append(x)
    else:
        odd_list1.append(x)
esum=0
osum=0

if(len(even_list1)>0):
    for e in even_list1:
        esum=esum+e
    print("even nos sum: ", esum)
    print("even nos max: ", max(even_list1))

if(len(odd_list1)>0):
    for o in odd_list1:
        osum=osum+o   
    print("odd nos sum: ", osum)
    print("odd nos max: ", max(odd_list1))


