# #sample input:hello world
# #sample output:world hello
# s=input()
# k=s.split()
# j=reversed(k)
# p=' '.join(j)
# print(p)





#program to modify string LOL!
# a="adarsh"
# a=a[:2]+"r"+a[3:]
# print(a)

     # OR




# a="adarsh"
# s=list(a)
# s[2]='r'
# a=''.join(s)
# print(a)

from turtle import position


string='abracadabra'
position=5
character='k'
string=string[:position]+character+string[position+1 :]
print(string)


