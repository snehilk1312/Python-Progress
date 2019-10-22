#Given an array, rotate the array to the right by k steps, where k is non-negative.  

#📌Example 1:
#Input: [1, 2, 3, 4, 5, 6, 7] and k = 3
#Output: [5, 6, 7, 1, 2, 3, 4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]


l=list(map(int,input().split()))
j=[]
k=int(input())
for a in range(k):
    j.insert(0,l.pop())
print(j+l)
