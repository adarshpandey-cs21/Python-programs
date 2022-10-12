a=int(input())
b=int(input())

for i in range(max(a,b),a*b+1):
    if i%a==0 and i%b==0:
        r=i
        break
print("lcm: ",r)