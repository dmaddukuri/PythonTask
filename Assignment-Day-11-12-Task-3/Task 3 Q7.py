""" 7. Write a program to replace the last element in a list with another list.
Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
Expected output: [1,3,5,7,9,2,4,6,8] """

list1 = [[1,3,5,7,9,10],[2,4,6,8]]
list2 =  list1[0]
list3 =  list1[1]
list2.pop()
list4 = list2+list3
print (list4)