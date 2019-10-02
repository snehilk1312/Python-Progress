'''The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.
Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of N
lowercase English letters. For a given integer K , you can select any K indices (assume

1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K
indices selected will contain the letter: 'a'. 

'''

n=int(input())
b=input().split()
m=int(input())
from itertools import combinations
k=list(combinations(b,m))
h=[]
for i in k:
    s=''
    s=s.join(i)
    h.append(s)
count=0
for i in h:
    if 'a' in i:
        count=count+1
print(count/len(h))
