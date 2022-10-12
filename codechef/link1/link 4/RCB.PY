
T = int(input())
for x in range(T):
    X,Y,Z=map(int,input().split())
    if Y<=(X+(2*Z)):
        print("YES")
    else:
        print("NO")
