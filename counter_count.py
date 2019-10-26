l=list(map(int,input().split()))
count=dict()
for i in l:
    count[i]=count.get(i,0)+1
print(count)

from collections import Counter
j=dict(Counter(l))
print('-----------\n',j)
