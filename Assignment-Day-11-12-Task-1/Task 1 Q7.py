# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?

a = 10
print(a)
print(type(a))

a = 45.5
print(a)
print(type(a))

# It over writes the new value everytime.

a = "Sample"
print(a)
print(type(a))