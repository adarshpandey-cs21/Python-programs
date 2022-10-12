# # # # # # # r,l=map(float,input().split())
# # # # # # # a=r*r*22/7
# # # # # # # v=a*l
# # # # # # # print(a)
# # # # # # # print(v)


# # # # # # l=[30,1,2,1,0]
# # # # # # print(l.index(1))
# # # # # # print(l.count(1))
# # # # # # print(len(l))
# # # # # # print(max(l))
# # # # # # print(min(l))
# # # # # # print(sum(l))


# # # # # matrix=[]
# # # # # matrix.append(3*[1])
# # # # # matrix.append(3*[5])
# # # # # matrix.append(3*[1])
# # # # # matrix[0] [0]=2
# # # # # print(matrix)


# # # # students={"peter","john"}
# # # # print(students)
# # # # students.add("john")
# # # # print(students)
# # # # students.add("peterson")
# # # # print(students)
# # # # students.remove("peter")
# # # # print(students)


# # # s1={1,4,5,6}
# # # s2={1,3,6,7}
# # # print(s1.union(s2))
# # # print(s1 | s2)
# # # print(s1.intersection(s2))
# # # print(s1 & s2)
# # # print(s1.difference(s2))
# # # print(s1-s2)
# # # print(s1.symmetric_difference(s2))
# # # print(s1^s2)


# # import pstats


# # try:
# #     a=5
# #     i=(input())
# #     l=[10,20,30,40]
# #     print(l[i])
# #     print(a)

# # except IndexError:
# #     print("error")
# # except:
# #     print("ki ho")
    
# # finally:
# #     print("hello")
# # print("bol")


fp=open("a.txt","r")
c=fp.read()
w=c.split()
fp=open("a.txt","r")
l=fp.readlines()
print("no. of caracter : ",len(c))
print("no. of words : ",len(w))
print("no. of lines",len(l))

