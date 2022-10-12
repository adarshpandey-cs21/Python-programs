# cook your dish here


#
T = int(input())
for x in range(T):
    A,B,C=map(int,input().split())
    k=min(A*B,A+C)
    print(k)


