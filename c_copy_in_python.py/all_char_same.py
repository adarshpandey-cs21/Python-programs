s=input("enter the string")
k=s.lower()
flag=0
l=len(k)

for i in k:
    for j in k:
        if j==i:
            flag+=1
    break
if flag==l:
    print("all case are same")
else:
    print("not same")

