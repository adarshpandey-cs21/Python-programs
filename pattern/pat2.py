row=int(input("enter row : "))
p=1
for i in range(1,row+1):
    for j in range(1,(row+1)-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    p+=1
    print()