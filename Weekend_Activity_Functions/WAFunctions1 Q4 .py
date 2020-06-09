#4. Write a program that accepts a hyphen-separated sequence of words as 
#input and prints the words in a hyphen-separated sequence after sorting them alphabetically.


inStr = input("Enter a hyphen-separated sequence of words: ")
l = inStr.split("-")
print(l)
l.sort()
print(l)