'''
The first line contains the space separated values of x and k .
The second line contains the polynomial P . 
Print True if P(x)=k . Otherwise, print False.
'''
x,k=list(map(int,input().split()))
j=input()
if eval(j)==k:
    print(True)
else:
    print(False)
