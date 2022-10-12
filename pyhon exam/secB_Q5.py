'''Write a Program to read a text file ‘sample.txt’ and prints only those
lines which starts with alphabet A. '''

fp=open("sample.txt","r")
k=fp.readlines()
s=''
for i in k:
    l=i.split()
    s=l[0]
    f=s[0]
    if f=='A':
        print(' '.join(l))