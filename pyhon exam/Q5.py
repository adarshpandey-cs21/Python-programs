'''Define the scope the variable in Python. What is the use of the 
nonlocal keyword, explain with the suitable examples?
Or
Define any four operators in Python which work with list or tuple. 
Write a Program to check whether given number is prime or not. (In 
Python-looping use while loop only)

'''


n=int(input())
count=0
m=n
while m>0:
    if n%m==0:
        count+=1
    m-=1
if count==2:
    print("prime")
else :
    print("not prime")
