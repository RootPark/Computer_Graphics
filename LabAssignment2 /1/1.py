import numpy as np

M = np.arange(5,21,1)
print(str(M)+'\n')

M=M.reshape(4,4)
print(str(M)+'\n')

M[1:3,1:3]=0
print(str(M)+'\n')

M=M@M
print(str(M)+'\n')

v=M[0,:]
print(np.sqrt(np.sum(v@v)))
