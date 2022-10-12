'''1. Read your name and check whether it is lucky name or not using function Lucky_Name(). Name is 
lucky name only if it contains all vowels (Not case sensitive)'''

def Lucky_Name(n):
    vowel={'a','e','i','o','u'}
    count=0
    for i in vowel:
        if i in n:
            count+=1
    if count==5:
        print("Lucky name")
    else:
        print("Not lucky")

n=input()
Lucky_Name(n)

'''2. Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s 
are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. 
Your function should ignore all other symbols that appear in s. Your function should return True if 
s has matched brackets and False if it does not.
Here are some examples to show how your function should work.
>>> matched("zb%78")
True
>>> matched("(7)(a")
False
>>> matched("a)*(?")
False
>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True
'''

#confusing




'''3. There is class of n students stored in a dictionary like roll numbers as a key and name as a values. I 
want to select some students for a trip with a condition as only those are allowed whose either name 
or roll no is lucky ( see que 1 and 2 for definition). Write a program for that.
'''


#not understandable