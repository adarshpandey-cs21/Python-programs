# # cook your dish
# T = int(input())
# for p in range(T):
#     D,C=map(int,input().split())
#     A1,A2,A3=map(int,input().split())
#     B1,B2,B3=map(int,input().split())    
#     if (A1+A2+A3) >=150 and (B1+B2+B3)>=150:
#         print("YES")
#     else:
#         print("NO")



# # cook your dish
# T = int(input())
# for p in range(T):
#     D,C=map(int,input().split())
#     A1,A2,A3=map(int,input().split())
#     B1,B2,B3=map(int,input().split())
#     A=A1+A2+A3
#     B=B1+B2+B3
#     K=A
#     L=B
#     if A<150:
#         K=A+D
#     if B<150:
#         L=B+D
#     if A>=150 
#     if (A+B+C)<(K+L):
#         print("YES")
#     else:
#         print("NO")


# cook your dish here
T=int(input())
for i in range(T):
    c,d=[int(i) for i in input().split()]
    A1,A2,A3=[int(i) for i in input().split()]
    B1,B2,B3=[int(i) for i in input().split()]
    sum=A1+A2+A3+B1+B2+B3
    x=2*c+sum
    y=d
    if((A1+A2+A3)>149):
        y=A1+A2+A3+y
    else:
        y=A1+A2+A3+y+c
    if((B1+B2+B3)>149):
        y=y+B1+B2+B3
    else:
        y=B1+B2+B3+y+c
    if(y<x):
        print("YES")
    else:
        print("NO")



# cook your dish here
t=int(input())
for i in range(t):
    c,d=[int(i) for i in input().split()]
    a1,a2,a3=[int(i) for i in input().split()]
    b1,b2,b3=[int(i) for i in input().split()]
    sum=a1+a2+a3+b1+b2+b3
    x=2*c+sum
    y=d
    if((a1+a2+a3)>149):
        y=a1+a2+a3+y
    else:
        y=a1+a2+a3+y+c
    if((b1+b2+b3)>149):
        y=y+b1+b2+b3
    else:
        y=b1+b2+b3+y+c
    if(y<x):
        print("YES")
    else:
        print("NO")