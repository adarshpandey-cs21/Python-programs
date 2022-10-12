'''1. Write a program that computes the net amount of a bank account based a transaction log from console 
input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

# t=int(input("enter total number of transaction : "))
# deposit=0
# debit=0
# for i in range(t):

#     l=input().split()
#     p=int(l[1])
#     if l[0]=='D':
#         deposit+=p
#     else:
#         debit+=p
# print(deposit-debit)


'''2. Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print all values except the first 5 elements in the list.
'''

#already done in previous set



'''3. Write a program that accepts a sentence and calculate the number of letters and digits in that 
sentence.
Suppose the following input is supplied to the program: hello world! 123 
Then, the output should be:
LETTERS - 10
DIGITS - 3'''

# n=input()
# alpha=0
# digit=0
# for i in n:
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         digit+=1
# print("letters : ",alpha)
# print("Digits : ",digit)