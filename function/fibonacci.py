def fibonacci(n):
    first=0
    second=1
    print(first)
    print(second)
    while(n>2):
        third=first+second
        first=second
        second=third
        print(third)
        n-=1
n=int(input("enter the length of fibonacci series"))
fibonacci(n)