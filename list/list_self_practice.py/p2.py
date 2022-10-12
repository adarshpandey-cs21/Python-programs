#Get the indices of all occurrences of an element in a list
n=int(input("enter the size of list : "))
print("enter the element in first list")
l1=[int(input()) for x in range (n)]

k=int(input("enter the element whose indcies you want to find"))

for i in range(len(l1)):
    if k==l1[i]:
        print(i)