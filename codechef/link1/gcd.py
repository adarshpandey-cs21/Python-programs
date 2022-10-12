#Solution Provided by CodingBroz
T = int(input())
for i in range(T):
    N= [int(x) for x in input().split(' ')]
    A = min(N)
    B = max(N)
    K= A*B
    while(B):
        A,B = B,A%B
    GCD = A
    LCM= K/GCD
    print(GCD,int(LCM))