'''
1. There are two file ‘file1.txt’ and ‘file2.txt’. Write a program to create a new file name ‘file3.txt’ that 
stores lines alternatively (one from file1 and one from file2) from both files. If content of any file 
finished in between then copy the remaining content of another file.
'''
#done

'''2. Write a program which create a dictionary using function in which keys are numbers between 1 and 
N (both included) and the values are square of keys. Print each item in separate lines. The function 
name is SQUARE() which accepts a number and return final dictionary '''
# def SQUARE(n):
#     d={i:i*i for i in range(1,n+1)}
#     return d

# n=int(input())
# k=SQUARE(n)

# for i in k:
#     print(i,k[i])


'''3. There are 10 students in a class. Some students’ names are same to other students. Write a python 
program to print the names that occur more than one time. The file name will be given by user 
where all names are written in a file as new line.
'''
k=input()
fp=open(k,"r")
l=fp.read()
l=l.split("\n")

k=set(l)
fp.close()
for i in k:
    if l.count(i) > 1:
        print(i)