'''
CALCULATIONS
Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.
COST(or total money earned)=$55+$45+$40+$60=$200
'''
import collections
X=int(input())
d=dict(collections.Counter(list(map(int,input().split()))))
N=int(input())
cost=0
for i in range(N):
    size,price=list(map(int,input().split()))
    if size in d:
        if d[size]!=0: 
            d[size]-=1
            cost+=price
        else:
            pass
    else:
        pass
print(cost)
