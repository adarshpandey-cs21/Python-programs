n=int(input("emter any number"))
first =0
second=1
print(first)
print(second)
while n>2:
    third=first+second
    first=second
    second=third
    n=n-1
    print(third)
