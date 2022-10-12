n=int(input())

for i in range(1,n):
    for k in range(1,n+1-i):
        print(" ",end='')

    for j in range(1,(2*i-1)+1):
        print("*",end='')
    print()


for i in range(n,0,-1):
    for k in range(1,n+1-i):
        print(" ",end='')

    for j in range(1,(2*i-1)+1):
        print("*",end='')
    print()


# n=int(input())
# k=1
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(k,end='')
#         k=k+1
#     print()
