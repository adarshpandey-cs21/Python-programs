T = int(input())
for p in range(T):
    N,K=map(int,input().split())
    L=list(map(int,input().split()))
    count=0
    for i in L:
        j=i+K
        if j%7==0:
            count+=1
    print(count)
        
        
        
    
