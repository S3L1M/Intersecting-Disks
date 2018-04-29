A = [1,5,2,1,4,0]
n = len(A)
C = 0
for i in range(n):
    for j in range(i+1, n):
        if A[i]+A[j]+i >= j :
            print "("+str(A[i])+" , "+str(A[j])+")"
            C += 1
print C
