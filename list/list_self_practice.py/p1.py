# #Remove common elements from two list in Python
n=int(input("enter the size of list : "))
print("enter the element in first list")
l1=[int(input()) for x in range (n)]
print("enter the element in second list")
l2=[int(input()) for x in range (n)]
# l1=[1,2,3,4,5,6,7,8,9,55]
# l2=[2,3,4,7,8,9,11,21,36]
for j in l2:
    if j in l1:
            l2.remove(j)
            l1.remove(j)
print(l1)
print(l2)