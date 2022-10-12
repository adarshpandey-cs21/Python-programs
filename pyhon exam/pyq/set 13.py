'''
1. Determine if a sentence is a pangram. A pangram is a sentence using every letter of the alphabet at 
least once. The best known English pangram is:
“The quick brown fox jumps over the lazy dog”.
The alphabet used consists of ASCII letters A to Z, inclusive, and is case insensitive. Input will not 
contain non-ASCII symbols.

'''
# n=input()
# n=n.lower()
# s="abcdefghijklmnopqrstuvwxyz"
# count=0
# for i in s:
#     if i in n:
#             count+=1
# if count==26:
#     print("pangram")
# else:
#     print("Not pangram")

'''2. Mr Khan is very lucky and having very good love life and so he decided to help numbers also to find 
their perfect love. According to him two numbers are in love with each other if their bitwise-xor and 
sum are equal.
For example: bitwise-xor of 160 and 75 is 235 and their sum is also 235. Hence 160 and 75 are 
perfect for each other. On the other hand the bitwise-xor of 32 and 63 is 31 but their sum is 95. Hence 
32 and 63 are not perfect for each other.
Write a program to help Mr. Khan in his task to Create a function name Perfect_Love() 
Which needs 2 numbers and print whether they are perfect for each other or not'''


# def Perfect_love(a,b):
#     if a+b == a^b:
#         print("perfect for each other")
#     else:
#         print("not perfect for each other")

# a=int(input())
# b=int(input())
# Perfect_love(a,b)


'''3. Write a program to read a file name data.txt and count number of lines words in each line in that file.
'''

# fp=open("data1.txt","r")
# l=fp.readlines()
# count =1 
# for i in l:
#     k=i.split()
#     print(f"number of words in line {count} = {len(k)}")
#     count+=1