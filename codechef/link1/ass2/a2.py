T=input()
for x in range(int(T)):
    N,K=map(int,input().split())
    D=list(map(int,input().split()))
    R=list(map(int,input().split()))
    sum=1000000000000000000000000000
    for i in range(len(D)):
        s=D[i]*K+R[i]
        if sum>s:
            sum=s
    print(sum)
        