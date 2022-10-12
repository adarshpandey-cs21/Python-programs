'''4
Write a Python program for the addition of two nested lists
(matrices) using List Comprehension'''


l=[[i for i in range(1,6)] for j in range(5) ]
m=[[i for i in range(1,6)] for j in range(5) ]

sum=[[l[j][i] + m[j][i] for i in range(len(l[0]))] for j in range(len(l))]

# print(l)
# print(m)
print(sum)