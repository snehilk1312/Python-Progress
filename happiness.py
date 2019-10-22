#There is an array of n integers. There are also disjoint sets,A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B . Your initial happiness is 0 . 
For each integer in the array, if  i element of A, you add 1 to your happiness. If element of B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end. 



happiness=0
n,m=list(map(int,input().split()))
k=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
for i in k:
    if i in A:
        happiness+=1
    if i in B:
        happiness-=1
print(happiness)
