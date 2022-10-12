file=open("b.txt","r")
a=file.readlines()
#k=a.split()
p=0
for i in a:
    if len(i)>p:
        p=len(i)
        long=i
print(long)

