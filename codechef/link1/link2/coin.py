T=int(input())
for i in range(T):
	N=int(input())
	i=0
	c=0
	while N-i>=0:
		i=i+1
		N=N-i
		c=c+1
	print(c)



T=int(input())
for X in range(T):
	A=int(input())
	p=0
	C=0
	while A-p>=0:
		p=p+1
		A=A-p
		C=C+1
	print(C)