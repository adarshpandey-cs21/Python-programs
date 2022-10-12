'''What is the difference between function read() and readline() in 
Python? Explain with a suitable example. Write a program to count 
the number of text lines in a text file 'info.txt' and display all lines on 
the console
'''

fp=open("info.txt","r")
k=fp.readlines()
p=''.join(k)
print(len(k))
print(p)