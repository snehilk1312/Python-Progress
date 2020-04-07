'''
https://www.hackerrank.com/challenges/py-collections-deque/problem
'''
from collections import deque
N=int(input())
d=deque()
for i in range(N):
    s=input()
    try:
        a,b=list(s.split())
        #print(a,b,sep='*')
        z='d.'+a+'(b)'
    except ValueError:
        a=s
        #print(a,end='*')
        z='d.'+a+'()'
    z=z.replace("'","")
    eval(z)
for i in d:
    print(i,end=' ')
