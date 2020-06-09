# 5.  Write a program that accepts a sequence of lines as input and prints the lines 
# after making all characters in the sentence capitalized.
# Sample input:
# Hello world 
# Practice makes perfect
# Expected Output:
# HELLO WORLD 
# PRACTICE MAKES PERFECT

def my_function(nlist):
    uList=[]
    for l in nlist:
        uList.append(l.upper())
    print(uList)


llines = ["Hello World","Practice makes perfect"]
my_function(llines)
