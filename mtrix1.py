import numpy as np
a = np.array([[2,45],[7,76],[9,34],[10,98],[5,87]])
mat = np.matrix(a)
with open('n_matrix.txt','wb') as f:
    for line in mat:
        np.savetxt(f,line,fmt='%.2f')
