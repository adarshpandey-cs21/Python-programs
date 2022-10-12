def fun(a):
    for i in a:
        j=k=i
        count=0
        sum=0
        while(j>0):
            j=j//10
            count+=1
        while(k>0):
            rem=k%10
            sum=sum+rem**count
            k=k//10
        if sum==i:
            print(f"{i} is armstrong")
        else:
            print(f"{i} is not armstrong")
a=[0,56,1,44,67,1,78,153,370,371,81,153]
fun(a) 