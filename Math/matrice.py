
L = [[1,3,0],
     [2,1,1],
     [1,1,0],
     [0,0,0]]
print(len(L))
M = L[0]

N = [[1,-1,0],
     [2,1,1],
     [0,1,0],
     [0,1,0]]


S = [[0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(L[0])):
    for j in range(len(L[0])):
               S[i][j] = L[i][j]+N[i][j]

print(S)
for ligne in S:
    print(ligne)

for ligne in L:
    print(ligne)

for ligne in N:
    print(ligne)

T=[[0 for j in range(5)]for i in range (4)]

for ligne in T:
    print(ligne)

A = [[0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0]]

for f in range(len(L[0])):
    for g in range(len(L[0])):
        A[f][g] = L[f][g]*5

print("_______________________")

for ligne in A:
    print(ligne)
