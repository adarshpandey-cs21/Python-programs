'''1. A disk drive shows T bytes and U bytes as free and used space respectively. If you delete a file of 
size O bytes and create a new file of size H bytes then how many free bytes will the disk have? 
Here T, U, O and H are user-entered values. Write a program in python to find the same
'''

# T=int(input("free space : "))
# U=int(input("used space : "))
# O=int(input("deleted fie size : "))
# H=int(input("created file soze : "))

# T=T+O-H
# print("free space available is : ",T)



'''2. Write a Python program that accepts a hyphen separated sequence of words as input and prints the 
words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items: green-red-yellow-black-white 
Expected Result: black-green-red-white-yellow '''

# s=input()
# l=s.split('-')
# l.sort()
# print('-'.join(l))



'''3. Write a program to create a new file name ‘mydata.txt’ and write your name, phone no, roll no and 
your branch in that file separated by space.
'''

# fp=open("mydata.txt","w")
# s='''Adarh Kumar Pandey
# 9955565603
# 2115000046
# B.Tech (CSE)
# '''
# fp.write(s)
# fp.close()