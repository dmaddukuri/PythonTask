# 8. 	Write a program in Python to iterate through the string “hello my name is abcde” 
# and print the string which has even length of word.


inStr = "hello my name is abcde"
x = inStr.split()
for i in x:
    if(len(i)%2 ==0):
        print(i)


