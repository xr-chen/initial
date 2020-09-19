import numpy as np

randR=np.random.normal(0,1,[10])
A=sorted(randR)
mid=(A[4]+A[5])/2
print(randR>mid)