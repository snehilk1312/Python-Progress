l=list()
n=int(input())
for i in range(1,n+1):
    if i==1:
        l.append(0)
    elif i==2:
        l.append(1)
    else:
        l.append(l[i-2]+l[i-3])
print(l)
