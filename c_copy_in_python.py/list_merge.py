l=[2,6,8,9]
m=[3,0,7,1]
list=[]
for i in range(len(l)):
    b=0
    c=0
    k=[]
    b=l[i]
    c=m[i]
    k.append(b)
    k.append(c)
    list.append(tuple(k))
print(list)

