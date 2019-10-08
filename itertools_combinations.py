'''
You are given a string S.
Your task is to print all possible combinations, up to size k , of the string in lexicographic sorted order.
'''


l=input().split()
m=[]
z=[]
from itertools import combinations
for i in range(1,int(l[1])+1):
    j=list(combinations(l[0],i))
    for w in j:
        #print(w)
        s=''
        w=sorted(w)
        s=s.join(w)
        #print(s)
        m.append(s)
        #print(m)
        m.sort()
    z+=m
        #print(z)
    m=[]
    j=[]
for a in z:
    print(a)
