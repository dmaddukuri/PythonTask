#3.Write a program to get the sum and multiply of all the items in a given list.

mul = 1
sum= 0

list1 = [1,2,3,4,5,6]
for i in list1:
    sum = i+sum
    mul = mul * i
    
print(sum)
print(mul)