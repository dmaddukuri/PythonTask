# 3. Create a function that takes a list and returns a new list
#  with unique elements of the first list.

def my_function(nlist):
  uList = set(nlist)
  print(uList)

nums = [2,2,2,1,1,3,3,4,5,6,5,4]
my_function(nums)