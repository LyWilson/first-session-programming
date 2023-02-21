def ProduitMat(A,B):
    p=len(A)
    q=len(A[0])
    r=len(B)
    s=len(B[0])
    if q==r:
        C=[[0 for j in range(s)]for i in range(p)]
        for i in range(p):
            for j in range(s):
                for k in range(q):
                    C[i][j]+=A[i][k]*B[k][j]
    return(C)
A=[[1,2,3],
   [3,4,5]]
B=[[1,2],
   [3,4],
   [5,6]]
C=ProduitMat(A,B)
for c in C:
    print(c)

def Transpose(A):
    p=len(A)
    q=len(A[0])
    T=[[0 for j in range(p)] for i in range(q)]
    for i in range(q):
        for j in range(p):
            T[i][j]=A[j][i]
    return(T)
T=Transpose(A)
for a in A:
    print(a)

for t in T:
    print(t)
