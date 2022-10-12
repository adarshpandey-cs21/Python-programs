# cook your dish here

T =int(input())
for x in range(T):
    N,X,P=map(int,input().split())
    M=X*3
    W=(N-X)*1
    T=M-W
    if T>=P:
        print("PASS")
    else:
        print("FAIL")
