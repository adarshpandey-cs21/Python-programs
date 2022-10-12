def lowercase(s):
    for i in s:
        c=ord(i)
        if c>=65 and c<=90:
            c=c+32
        print(chr(c),end='',sep='')
s=input("enter string in uppercase")
lowercase(s)
