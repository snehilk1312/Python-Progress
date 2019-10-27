'''
Print the averages of all students on separate lines.
The averages must be correct up to 1 decimal place.

SAMPLE INPUT:
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

SAMPLE OUTPUT:
90.0 
91.0 
82.0 
90.0 
85.5   
'''

N,X=list(map(int,input().split()))
s=[]
for i in range(X):
    l=list(map(float,input().split()))
    s.append(l)
u=[]
count=0
for a in range(N):
    m=[]
    for i in s:
        m.append(i[count])
    u.append(m)
    count+=1
for i in u:
    print(sum(i)/X)
