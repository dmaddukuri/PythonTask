# 11. 	Write a program to find out the occurrence of a specific word from an alphanumeric statement.
#  Example: 12abcbacbaba344ab  
#  Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

x = "12abcbacbaba344ab" 
all_freq = {} 

for i in x: 
    if(i.isalpha()):
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1

print(all_freq)