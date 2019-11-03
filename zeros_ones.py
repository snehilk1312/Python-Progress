import numpy as np
a=tuple(map(int,input().split()))
print(np.zeros(a,dtype=np.int32),np.ones(a,dtype=np.int32),sep='\n')  #a is tuple and like size,i.e (3,3,3)
