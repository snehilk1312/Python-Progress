'''
https://www.hackerrank.com/challenges/matrix-script/problem
'''
import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
u=[]
for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)
print(matrix)
for a in range(m):
    for i in matrix:
        u.append(i[a])
t=''.join(u)
print(t)
s=''
#pattern=r'\W+'
pattern=r'(?<=\w)((\W+)(?=\w))'
s=re.sub(pattern,' ',t)
print(s)
