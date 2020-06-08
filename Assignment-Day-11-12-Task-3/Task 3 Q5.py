#5. Create a new list which contains the specified numbers
#  after removing the even numbers from a predefined list. 

list1 = [11,25,42,62,73,83]
list2 = list1.copy()
num = 0
for i in list1:
    num = i
    if(num%2 == 0):
        list2.remove(i)
print(list2)