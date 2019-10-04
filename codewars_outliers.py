def find_outlier(integers):
    l=[]
    for j in integers:
        if j%2==0:
            l.append(j)
    if len(l)==1:
        res=list(filter(lambda x:x%2==0,integers))        
    else:
        res=list(filter(lambda x:x%2!=0,integers))
    for i in res:
        return i
l=[1,2,4,6,8,10]
print(find_outlier(l))
