'''
1. The mumbai city local train system carries 2,75,000 people each day. The train system observes 
15% growth in rainy season only for a particular period (in months) entered by user. How many 
people does the train system carry each year? Write a program in python for the same.
'''

# Passenger=275000
# n=int(input("Enter rainy period in months : "))
# tday=365
# lday=365-n*30

# growth=Passenger*0.15
# tgrowth=Passenger+growth

# tpass_in_year=Passenger*lday+tgrowth*n*30
# print("total passenger in year : ",tpass_in_year)


'''2. Create first dictionary name ‘ASC_Value’ in python using loop in which keys are alphabets (Lower 
case letters) and values are their corresponding ASCII code. Print the final dictionary items in 
separated lines. Also read your first name and calculate your ASCII score (add ASCII code of each 
character of your name) using that dictionary ASC_Value.'''


# asc_value={}
# s="abcdefghijklmnopqrstuvwxyz"
# for i in s:
#     asc_value[i]=ord(i)
# print(asc_value)

# score=0
# n=input("Enter your name : ")
# for i in n:
#     score=score+ord(i)
# print(score)


'''
3. There is a file name ‘DATA.txt’ which stores some data. Write a program that read the content of 
that file and count how many lines, words, alphabets and digits are there in this file'''

fp=open("DATA.txt","r")
c=fp.read()
w=c.split()
fp.close()
alpha=0
dig=0
for i in c:
    if i.isalpha():
        alpha=alpha+1
    elif i.isdigit() :
        dig+=1

fp=open("DATA.txt","r")
l=fp.readlines()
print("no. of alphabet : ",alpha)
print("no. of digit : ",dig)
print("no. of words : ",len(w))
print("no. of lines : ",len(l))
fp.close()