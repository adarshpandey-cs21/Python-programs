def sumsquare(l):
    list=[]
    odd=0
    even=0
    for i in l:
        if i%2!=0:
            odd+=i*i
        elif i%2==0:
            even+=i*i
    list.append(odd)
    list.append(even)
    return list


l=[1,3,5]
# l1=[2,4,6]
# l2=[-1,-2,3,7]
k=sumsquare(l)
print(k)

# m=sumsquare(l1)
# print(m)

# n=sumsquare(l2)
# print(n)
            
