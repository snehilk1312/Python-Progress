'''
https://www.hackerrank.com/challenges/ginorts/problem
'''
s=input()
a,b,c,e=[],[],[],[]
for i in s:
    if i.isupper():
        b.append(i)
    elif i.islower():
        a.append(i)
    else:
        if int(i)%2!=0:
            c.append(i)
        else:
            e.append(i)
a=sorted(a)
b=sorted(b)
c=sorted(c)
e=sorted(e)
d=a+b+c+e
a=''.join(d)
print(a)
