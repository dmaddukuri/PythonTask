""" Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
Expected Result: {1:10,2:20,3:30,4:40} """


a={1:10,2:20}
b={3:30,4:40}

thisdict =dict(a)
print(thisdict)
for i in b:
    thisdict[i] = b[i]
print(thisdict)