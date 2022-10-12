row=int(input())
col=int(input())
# m=[int(input()) for j in range(col) for i in range(row)]
# d={}
# for i in range(row):
#     for j in range(col):
#         d[(i,j)]=m[i][j]
# print(m)
# print(d)

m=[int(input()) for j in range(col) for i in range(row)]
d={(i,j):m[i][j] for j in range(col) for i in range (row)}  
print(m)
print(d)