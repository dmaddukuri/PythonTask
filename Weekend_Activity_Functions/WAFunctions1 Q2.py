#2. Write a function that accepts a string and calculate 
# the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def my_function(str):
    upperCnt=0
    lowerCnt=0
    for i in str:
        if(i.islower()):
            lowerCnt=lowerCnt+1
        if(i.isupper()):
            upperCnt=upperCnt+1
    print("No. of Upper case characters : ",upperCnt)
    print("No. of Lower case Characters : ",lowerCnt)



my_function("EmilRefsnes")