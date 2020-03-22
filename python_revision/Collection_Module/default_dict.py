n,m = list(map(int, input().split()))

from collections import defaultdict
d=defaultdict()
g=defaultdict()
for i in range(n):
    d[i]=input()

for i in range(m):
    g[i]=input()


for k,v in g.items():
    flag=0
    l=[]
    for k2,v2 in d.items():
        if v==v2:
            flag=1
            l.append(k2+1)
    if flag==0:
        l.append(-1)   
    for u in l:
        print(u,end=' ')
    print()
