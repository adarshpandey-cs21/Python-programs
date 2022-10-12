''' 1. Mr. Samuel Gene is purchasing items for his relatives. He has purchased the following items:
• 3 shirts, at the rate of 680 rupees
• 1 computer game, at the rate of 750 rupees
• 2 bracelets, at the rate of 230 rupees
Write a program to find the total cost. Later he returned one of the bracelet for a full refund and 
one shirt at a loss of 50%. Find the total cost after refund using the same program
'''


# shirt=680
# game=750
# bracelets=230

# total_cost=3*shirt+game+2*bracelets
# print("total cost : ",total_cost)

# refund=(0.50*shirt) + bracelets

# total_cost_after_refund=total_cost-refund

# print("total cost after refund : ",total_cost_after_refund)



'''2. Create a File name ‘info.txt’ that stores n random generated numbers in separate lines. After that 
read the content of this file and print average of these n numbers.'''


# import random
# n=int(input("enter total number : "))
# fp=open("info.txt","w")
# for i in range(n):
#     a=random.randint(1,1000)
#     fp.write(str(a)+ '\n')
# fp.close()

# fp=open("info.txt","r")
# s=fp.read()
# l=list(map(int,s.split()))
# print("average of generated number is : ",sum(l)/n)


'''3. Given a string, return a "rotated right" version where the last n chars are moved to the start. The 
string length will be at least 2.
right2("Hello",2) → "loHel" 
right2("java",3) → "avaj"
right2("Hi",3) → "Hi"'''

# n=input()
# k=int(input())
# m=len(n)


# if m-k<0:
#     print(n)
# else:
#     p1=n[m-k:]
#     p2=n[0:m-k]
#     print(p1+p2)



