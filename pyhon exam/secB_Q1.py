'''Polycarp has n coins, the value of the i-th coin is ai. Polycarp wants 
to distribute all the coins between his pockets, but he cannot put two 
coins with the same value into the same pocket.
For example, if Polycarp has got six coins represented as an array
a=[1,2,4,3,3,2], he can distribute the coins into two pockets as 
follows: [1,2,3],[2,3,4].
Polycarp wants to distribute all the coins with the minimum number 
of used pockets. Help him to do that.
Input
The single line of the input contains n integers space separated a1 
a2. (1≤ai≤100) values of coins.
Output
Print only one integer — the minimum number of pockets Polycarp 
needs to distribute all the coins so no two coins with the same value 
are put into the same pocket.
Examples
Input0             Input1
1 2 4 3 3 2       64 100
Output 2           Output 1'''


l=list(map(int,input().split()))
s=set(l)
count=0
for i in s:
    if l.count(i) > count:
        count=l.count(i)
print(count)
