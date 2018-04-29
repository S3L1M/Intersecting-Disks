import numpy as np

A = [1,5,2,1,4,0]
n = len(A)
R = np.ones((n,n), dtype=int)       #[[1 for i in range(n)] for j in range(n)]
nR = n * (n - 1)
cc = 0
for i in range(n):
    for j in range(i+A[i]+1, n):
        if (A[i] + A[j] + i < j+1):
            R[i][j] = R[j][i] = 0
            nR -= 2 
            cc += 1
print nR/2
print R
