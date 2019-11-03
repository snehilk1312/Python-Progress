'''
https://www.hackerrank.com/challenges/py-set-mutations/problem
'''
n=int(input())
b=set(map(int,input().split()))
m=int(input())
for i in range(m):
    a,d=input().split()
    c=set(map(int,input().split()))
    getattr(b,a)(c)
print(sum(b))
