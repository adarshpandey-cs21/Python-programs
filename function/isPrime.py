def isPrime(n):
    flag=0
    for i in range(1,n+1):
        if n%i==0:
            flag+=1
    if flag==2:
        return True
    else:
        return False
n=int(input("enter to check prime"))
z=isPrime(n)
print(z)