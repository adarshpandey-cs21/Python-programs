n=int(input())
fp=open("sample.txt","r")
p=fp.readlines()
k=p[len(p)-n: ]
print(''.join(k))