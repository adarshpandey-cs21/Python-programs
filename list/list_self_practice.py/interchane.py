# #using function
# def swaplist(list):
#     n=len(list)
#     temp=list[0]
#     list[0]=list[n-1]
#     list[n-1]=temp

#     return list

# l=[22,4,6,87,71]

# k=swaplist(l)
# print(k)
# t=swaplist(l)
# print(k)
# print(t)






# #using method


# l=[33,65,89,54]
# last=l.pop()
# first=l.pop(0)

# l.insert(0,last)
# l.append(first)
# print(l)





#interchasnge when position is given

l=[44,61,67,89,32,46,7]
p1=2
p2=5
k=l.pop(p1-1)
n=l.pop(p2-2)

l.insert(p1-1,n)
l.insert(p2-1,k)
print(l)