'''1. Write a program that calculates and calculate the value according to the given formula: 
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.
D is a list whose values should be input to your program in a comma separated sequence. 
Create a new list of calculated Q for each value of D
Example
Comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24  '''

# D=list(map(int,input().split(",")))
# Q=[]
# C=50
# H=30
# for i in D:
#     k=int(((2*C*i)/H)**0.5)
#     Q.append(k)
# print(Q)


'''2. Write the program where the user enters a string and a substring. You have to print the number of 
times that the substring occurs in the given string. String traversal will take place from left to right, 
not from right to left.
NOTe String letters are case-insensitive.
 '''

# s=input()
# s=s.lower()
# ss=input()
# ss=ss.lower()

# print(s.count(ss))

'''3. Write the program to print the multiplication table from 1 to 10 in file table.txt as each multiple of a 
number separated by space and every table will be in new line.
'''

# fp=open("table.txt","w")
# for i in range(1,11):
#     if i==1:
#         for j in range(10):
#             fp.write(str(i+j)+' ')
#         fp.write('\n')
#     else:
#         for k in range(1,11):
#             fp.write(str(i*k)+' ')
#         fp.write('\n')

# fp.close()
