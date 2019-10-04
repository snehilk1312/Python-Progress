def longest(s1, s2):
    a=set()
    b=set()
    for i in s1:
        if not (i.isalpha() and i.islower()):
                continue
        a.add(i)
    for i in s2:
        if not (i.isalpha() and i.islower()):
                continue
        b.add(i)
    k=list(a|b)
    k.sort()
    l=''
    l=l.join(k)
    return (l)
s1=input()
s2=input()
print(longest(s1,s2))
