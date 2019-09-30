'''
You are given words. Some words may repeat.
For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
'''
from collections import Counter
n=int(input())
l=[]
for i in range(n):
    k=input()
    l.append(k)
g=set(l)
print(len(g))
m=Counter(l)
for key,value in m.items():
    print(value,end=' ')
