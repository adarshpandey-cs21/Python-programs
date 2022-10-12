a=(2,4,7,9,3)
b=(4,6,8,9,3)
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(j)
print(tuple(c))

