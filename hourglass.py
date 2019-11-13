b,m,l=[],[],[]
rows=int(input())
for i in range(rows):
    a=list(map(int,input().split()))
    b.append(a)

for c in range(rows-2):
    for e in range(len(a)-2):
        m.append([b[c][0+e],b[c][1+e],b[c][2+e],b[c+1][1+e],b[c+2][0+e],b[c+2][1+e],b[c+2][2+e]])
for i in m:
    l.append(sum(i))
print(max(l))
