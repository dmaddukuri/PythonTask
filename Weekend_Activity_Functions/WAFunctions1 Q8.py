# 8. Define a function which can generate and print a tuple where the value 
# are square of numbers between 1 and 20.

def my_function():
    numL = list()
    for i in range(1,21):
        numL.append(i**2)
    #print(numL)
    numT=tuple(numL)
    print(numT)

my_function()
