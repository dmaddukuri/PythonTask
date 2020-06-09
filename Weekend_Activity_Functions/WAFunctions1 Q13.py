# 13. Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] 
# using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 

from functools import reduce

def addL(x,y):
    return x+y

inList = [[1,2,3],[4,5],[6,7,8]]
opList = reduce(addL, inList)

print(opList)