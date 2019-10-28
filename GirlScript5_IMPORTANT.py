'''
FINDING LONGEST PALINDROMIC SUBSTRING IN THE STRING.
'''
import itertools
s=input()
l,m,u=[],[],[]
for i in range(1,len(s)+1):
    for j in range(i):
        s_=s[j:i]
        l.append(s_)
for i in l:
    if i==i[::-1]:
        m.append(i)
for i in m:
    u.append(len(i))
z=list(zip(u,m))
z=sorted(z)
print(z[-1][1])
