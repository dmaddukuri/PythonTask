# 3. Swap two numbers using the third variable as the result name and do the same task without using any third variable.

x = 5
y = 10

print(x)
print(y)

 #Swapping with third variable 
z = y
y = x
x = z
print(x)
print(y)

# Swapping without thrid variable
x = x+y
y = x-y
x = x-y

print(x)
print(y)