# cook your dish here
T = int(input())
for x in range(T):
    N,K = map(int, input().split())
    sum=0
    for p in range(1,K+1):
        sum=max(sum,N%p)
    print(sum)
