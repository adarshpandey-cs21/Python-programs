
T = int(input())
for x in range(T):
    M,N,K=map(int,input().split())
    if M>(N*K):
        print("YES")
    else:
        print("NO")
