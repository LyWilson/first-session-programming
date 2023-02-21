M=[[0,1,1,1,0],
   [0,1,0,0,0],
   [0,1,1,0,0],
   [0,1,0,0,0],
   [0,1,0,0,0]]

A=[[0,0,0,0,1],
   [0,0,0,1,0],
   [0,0,1,0,0],
   [0,1,0,0,0],
   [1,0,0,0,0]]

B=[[0,1,0,0,0],
   [0,0,1,0,0],
   [0,0,0,1,0],
   [0,0,0,0,1],
   [0,0,0,0,0]]

def Transpose(M):
    p=len(M)
    q=len(M[0])
    T=[[0 for j in range(p)] for i in range(q)]
    for i in range(q):
        for j in range(p):
            T[i][j]=M[j][i]
    return(T)

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

print("numere 1-a---------------------")

#a)
for i in M:
    print(i)

print("numere 1-b---------------------")

#b)                   
T=Transpose(M)
for m in T:
    print(m)

print("numere 1-c---------------------")

#c)
for k in ProduitMat(A,M):
    print(k)
    #symetrie horizontal

print("---------------------")

for h in ProduitMat(M,A):
    print(h)
    #symetrie vertical
print("numere 1-d---------------------")

#d)
for y in ProduitMat(B,M):
    print(y)
    #enlever premiere liste et ajouter un nouvelle liste de zero a la fin / il decale de 1 vers le haut

print("---------------------")

for u in ProduitMat(M,B):
    print(u)
    #decaler de une colonne vers la droite / le dernier chiffre de chaque liste est deplacer en premiere possition de chaque liste
    
print("numere 1-e---------------------")

#e)
for n in ProduitMat(ProduitMat(A,M),B):
    print(n)
    #la matrice a fait une symetrie horizontal et elle est decaler de 1 vers la droite

print("numere 1-f---------------------")

#f)
for m in ProduitMat(ProduitMat(ProduitMat(ProduitMat(ProduitMat(A,M),B),A),B),B):
    print(m)
    #pour obtenir cette matrice nous devons faire (((((A*M)*B)*A)*B)*B)
