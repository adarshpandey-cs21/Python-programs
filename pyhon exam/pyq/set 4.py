'''1. Write a program that accepts a comma separated sequence of words as input and prints the words in a 
comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
Input: without,hello,bag,world 
Then, the output should be:
bag,hello,without,world'''


# n=input()
# a=n.split(',')
# a.sort()
# print(','.join(a))


'''2. Write a Python program that count number of upper case and lower case letters in a given file name 
‘data.txt’ using function name COUNT_CASE() that accepts file data as input and return the number 
of uppercase letters and lowercase letters.
Sample Data in file: 'The quick Brow Fox' 
Expected Output:
No. of Upper case characters: 3 
No. of Lower case Characters: 12'''

# def COUNT_CASE(s):
#     lc=0
#     uc=0
#     for i in s:
#         if ord(i)>=97 and ord(i)<=122:
#             lc+=1
#         elif ord(i)>=65 and ord(i)<=90:
#             uc+=1
#     print("No. of Upper case characters: ",uc)
#     print("No. of lower case characters: ",lc)

# fp=open("DATA.txt","r")
# s=fp.read()
# COUNT_CASE(s)


'''3. Write a program to create a dictionary name ‘data’ which stores 10 students name along with their 
marks in Python Programming subject. Print dictionary items in separated line and then average 
marks obtained by these 10 students in this subject in last line '''


# data={input("enter name : ") : int(input("enter marks : ")) for i in range(10)}
# sum=0
# for i in data:
#     print(i,data[i])
#     sum+=data[i]
# print("average : ",sum/10)
