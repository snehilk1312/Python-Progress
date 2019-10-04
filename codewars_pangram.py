import string

def is_pangram(s):
    l=s.split()
    k=''
    m=set()
    k=k.join(l)
    for i in k:
        if i.isalpha():
            m.add(ord(i.lower()))
        else:
            continue
    p=[x for x in range(ord('a'),ord('{'))]
    n=list(m)
    n.sort()
    p.sort()
    if n==p:
        return True 
    else:
        return False
s='ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'
print(is_pangram(s))
