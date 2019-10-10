'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

'''
from itertools import combinations
def is_sum(j):
    flag=0
    for i in j:
        if sum(i)==k:
            flag=1
            return True
    if flag==0:
        return False

l=list(map(int,input().split()))
k=int(input())
j=list(combinations(l,2))
print(is_sum(j))
