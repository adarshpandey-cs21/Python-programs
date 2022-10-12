# s=input().split()
# vol="aeiouAEIOU"
# l=[]
# for i in s:
#     k=len(i)
#     if i[0] not in vol and i[k-1] in vol:
#         l.append(i)

# print(' '.join(l))


# l=[]
# for i in range(1,1001):
#     for j in range(2,10):
#         if i%j==0:
#             l.append(i)
#             break
# list=[i for i in l]
# print(list)


# x=int(input())
# y=int(input())
# if y/x==2:
#     print("yes")
# else:
#     print("no")


# fp=open("gla.txt","a")
# s="Dont gamble on the future,act now,without delay"
# fp.write(s)




# import random
# import numpy
# l=[]
# for i in range(200):
#     l.append(1)
# for i in range(100):
#     l.append(0)
# for i in range(180):
#     l.append(6)
# l1=random.sample(l,len(l))
# a=numpy.array(l1)
# b=numpy.reshape(a,(8,60))
# print(b)
# print(b.shape)


# def issorted(ls : list)->int:
#     l=ls[::]
#     l.sort()
#     if l==ls:
#         return 0
#     #l.sort(reverse=True)
#     elif l==ls:
#         return 1


# fp=open("pallindrome.txt","w")
# for i in range(1000,10000):
#     j=i
#     sum=0
#     while j>0:
#         rem=j%10
#         sum=sum*10+rem
#         j=j//10
#     if sum==i:
#         fp.write(str(sum)+'\n')
    
