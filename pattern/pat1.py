row=int(input("enter row : "))
for i in range(row,0,-1):
    for j in range(i):
        print("*",end="")
    print()