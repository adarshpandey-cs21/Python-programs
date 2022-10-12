
# T = int(input())
# tests = []
# for i in range(T):
#     tests.append([int(i) for i in input().split()])
# for i in tests:
#     print(i[0]%i[1])




# T = int(input())
# for x in range(T):
#     A,B = map(int, input().split())
#     print(A % B

T = int(input())
for x in range(T):
    A,B = map(int, input().split())
    for i in range(1,min(A,B)+1):
        if A%i==0 and B%i==0:
            GCD=i
    for i in range(max(A,B),A*B+1):
        if i%A==0 and i%B==0:
            LCM=i
            break
    print(GCD,LCM,sep=' ')






#to find second max
# T = int(input())
# for x in range(T):
#     A,B,C=map(int,input().split())
#     list=[]
#     list.append(A)
#     list.append(B)
#     list.append(C)
#     list.sort()
#     print(list[1])



#mahasena

# T = int(input())
# list=[]
# list=[int(i) for i in input().split()]
# odd=0
# even=0
# for J in list:
#    if J%2==0:
#         even+=1
#    else:
#         odd+=1
# if even>odd:
#     print("READY FOR BATTLE")
# else:
#     print("NOT READY")





