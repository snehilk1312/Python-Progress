import itertools
def lcs(x,y):
    k=[]
    l=[]
    h=''
    j=''
    for i in range(len(x)):
        k+=itertools.combinations(x,i+1)
    for i in range(len(y)):
        l+=itertools.combinations(y,i+1)
    for i in k:
        if i in l:
            j=i
    for i in j:
        h+=i
    return h
x=input()
y=input()
print(lcs(x,y))
