#7.  Define a function that can accept two strings as input and 
# print the string with maximum length in console. 
# If two strings have the same length, 
# then the function should print all strings line by line.

def my_function(str1, str2):
    l1=len(str1)
    l2=len(str2)
    if(l1>l2):
        print(str1)
    elif(l2>l1):
        print(str2)
    else:
        print("all strings line by line")

my_function("happy", "morning")