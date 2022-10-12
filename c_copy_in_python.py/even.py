n=int(input("enter the size of list: "))
a=[]
for j in range(0,n):
    print("enter the element ")
    k=int(input())
    a.append(k)
sum=0
print(a)
for i in a:
    if i%2==0:
        sum=sum+i
print(sum)