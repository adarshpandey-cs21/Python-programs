for _ in range(int(input())):
    N,S=map(int,input().split())
    if(S<=N):
        print(S)
    else:
        print(abs((2*N)-S))
