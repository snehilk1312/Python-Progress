'''
You are given a string  S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S  that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.
'''
s=input()
import re
m=[]
for l in s:
    if l not in ['A','E','I','O','U','a','e','i','o','u']:
        m.append(l)
        m.append(l)
    else:
        m.append(l)
b=''
b=b.join(m)
#print(b)
k=re.findall('[^a,e,i,o,u,A,E,I,O,U]([a,e,i,o,u,A,E,I,O,U]{2,})[^a,e,i,o,u,A,E,I,O,U]',b)
#print(k)
if len(k)!=0:
    for i in k:
        print(i)
else:
    print(-1)
