'''
Explain the difference between the list comprehension and 
dictionary comprehension with suitable examples. Write a Python 
Program to find the frequency of each character in string using 
dictionary comprehension.
Sample input 
banana
Sample Output
{‘b’: 1, ‘a’: 3, ‘n’: 2}
'''

s=input()
#l=list(s)
t=set(s)
d={}

for i in t:
    p=s.count(i)
    d[i]=p
print(d)

