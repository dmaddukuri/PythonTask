# Write a program in Python to reverse a string and print only the vowel 
# alphabet if exist in the string with their index.


x = "consulatadd"
print(x)
x=x[::-1]
print(x)
cnt =0
for i in x:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        print(i+" "+str(cnt))
    cnt=cnt+1

    



