'''

LINK:
https://www.hackerrank.com/challenges/python-sort-sort/problem
INPUT:
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity. 

OUTPUT:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''
nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input())
arr.sort(key= lambda arr:arr[k])
for i in arr:
    i=list(map(str,i))
    s=' '
    s=s.join(i)
    print(s)
