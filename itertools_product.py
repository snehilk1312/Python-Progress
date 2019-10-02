from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
k=list(product(A,B))
print(*k)
