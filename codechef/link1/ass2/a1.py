T = int(input())
for x in range(T):
    N=int(input())
    M=N
    sum=0
    while M>0:
        r=M%10
        sum+=r
        M=M//10
    if N%sum==0:
        print("Yes")
    else:
        print("No")
        