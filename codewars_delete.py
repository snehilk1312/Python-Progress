def delete_nth(order,max_e):
    l=[]
    for i in order:
        k=l.count(i)
        print(k)
        if k<max_e:
            l.append(i)
            print(l)
        else:
            continue
    return l
p=[20,37,20,21]
q=1
print(delete_nth(p,q))
