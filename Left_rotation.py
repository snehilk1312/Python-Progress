'''
https://www.hackerrank.com/challenges/array-left-rotation/problem

'''

n,d=list(map(int,input().split()))
j = list(map(int,input().split()))
print(j)
m=[]
l=d
for i in range(len(j)-d):
    m.append(j[l])
    l=l+1
m=m+j[0:d]
k=' '
m=list(map(str,m))
k= k.join(m)
print(k)
