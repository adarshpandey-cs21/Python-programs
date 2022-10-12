T = int(input())
for k in range(T):
    X,Y,x,y,D=map(int,input().split())
    if (x*D)<=X and (y*D)<=Y:
        print("YES")
    else:
        print("NO")
