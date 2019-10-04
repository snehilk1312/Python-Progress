sentence='gol2a loal1 chol3'
dict={}
m=[]
g=[]
h=' '
l=sentence.split()
for i in l:
    for j in i:
      if j.isnumeric():
          dict[j]=i
for i in dict.keys():
    m.append(i)
m.sort()
for i in m:
    g.append(dict[i])
h=h.join(g)
print(h)
