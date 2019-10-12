'''
A valid mobile number is a ten digit number starting with a 7,8 or 9 .
'''

N=int(input())
l=[]
import re
for i in range(N):
    k=input()
    if len(k)!=10:
        print('NO')
    else:
        k=re.match(r'[7-9]\d{9}',k)
        if k:
            print('YES')
        else:
            print('NO')
