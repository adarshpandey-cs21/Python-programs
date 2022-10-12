

T = int(input())
for x in range(T):
    l=list(map(int,input().split()))
    sunny=0
    rainy=0
    for i in l:
        if i==1:
            sunny+=1
        else:
            rainy+=1
    if sunny>rainy:
        print("YES")
    else:
        print("NO")


