s=input()
for i in range (len(s)):
    if s[i]>='A' and s[i] <='Z':
        x=ord(s[i])
        x=x+32
        y=chr(x)
        print(y,end='',sep='')

    if s[i]>='a' and s[i] <='z':
        x=ord(s[i])
        x=x-32
        y=chr(x)
        print(y,end='',sep='')

