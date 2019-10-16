import numpy as np
l=list(map(int,input().split()))
k=np.array(l)
#print(k)
print(np.reshape(k,(3,3)))   #converts 1-D array into 3-D array usin reshape function
