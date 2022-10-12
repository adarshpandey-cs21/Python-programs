# cook your dish here
T = int(input())
for x in range(T):
    N,X,Y=map(int,input().split())
    A=list(map(int,input().split()))
    count=0
    for i in A:
        if i<=X and i%Y==0:
            count+=1
    print(count)
