'''
https://www.hackerrank.com/challenges/compress-the-string/problem
'''
from itertools import groupby
s=input()
my_list=[list(g) for k, g in groupby(s)]
print(my_list)
keys=[k for k, g in groupby(s)]
print(keys)
for i in my_list :
    print("({}, {})".format(len(i), i[0]), end=' ')

