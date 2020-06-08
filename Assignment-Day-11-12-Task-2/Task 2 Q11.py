""" In the previous question, insert “break” after the “Good guess!” print statement. 
“break” will terminate the while loop so that users do not have to continue guessing after they found the number. 
If the user does not guess the number at all, print “Sorry but that was not very successful”.

"""
counter=1
answer= 9
i=0
while counter<=5:
	number = int(input("Type in the " + str(counter) + " number (1-9):"))
	if(number==answer):
		print("Good guess!")
		break
	else:
		print("Try again!")
	if(counter == 5):
		print("Sorry but that was not very successful")
		break
	counter = counter+1
