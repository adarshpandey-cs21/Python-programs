
n=int(input("enter the no. to be checked : "))
m=n
l=n
count=0
sum=0
while n>0:
    n=n//10
    count+=1
while m>0:
    rem=m%10
    sum+=rem**count
    m=m//10
if l==sum:
    print("Armstrong")
else:
    print("Not armstrong")
