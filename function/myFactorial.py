def myFactorial(n):
    fact=1
    while(n>0):
        fact=fact*n
        n-=1
    return fact
n=int(input("enter the number to check factorial"))
z=myFactorial(n)
print(z)