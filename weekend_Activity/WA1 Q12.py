# 12. Generate and print another tuple whose values are even numbers 
# in the given tuple (1,2,3,4,5,6,7,8,9,10).

thistuple = (1,2,3,4,5,6,7,8,9,10)
x=[]
for i in thistuple:
    if(i%2==0):
        x.append(i)

print(x)

print(tuple(x))

