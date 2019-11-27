'''
https://www.hackerrank.com/challenges/python-power-mod-power/problem

hint:
possible to calculate pow(a,b) = a**b
possible to calculate pow(a,b,c) = (a**b) mod c
'''

a = int(input())
b = int(input())
c  =int(input())
d = pow(a,b)
e = pow(a,b,c)
print(d,e,sep='\n')
