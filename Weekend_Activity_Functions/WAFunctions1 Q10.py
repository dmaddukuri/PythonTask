#10. Write a program which can filter() to make a
#  list whose elements are even number between 1 and 20 ( both included)

def filter():
    evenList=[]
    for i in range(1,20+1):
        if i%2 == 0:
            evenList.append(i)
    print(evenList)

filter()