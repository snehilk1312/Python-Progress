'''You are given a function f(X)=X^2.
You are also given K lists. The ith list consists of N(i) elements.
You have to pick one element from each list so that the value from the equation below is maximized:
S=(f(X1)+f(X2)+f(X3)+...+f(XK))%M
Xi denotes the ith element picked from the list . Find the maximized Smax value obtained. 
%  denotes the modulo operator.Note that you need to take exactly one element from each list, not necessarily the largest element. 
Youadd the squares of the chosen elements and perform the modulo operation. 
The maximum value that youcan obtain, will be the answer to the problem.
'''


import itertools
k=list(map(int,input().split()))
#print(k)
g=[]
h=[]
for i in range(k[0]):
    m=list(map(int,input().split()))
    m.remove(m[0])
    g.append(m)
#print(g)
u=list(itertools.product(*g))
#print(u)
for i in u:
    f=sum(map(lambda x:x**2,i))%k[1]
    h.append(f)
print(max(h))
