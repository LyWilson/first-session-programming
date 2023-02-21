Gris = [[0,0,0,0],
        [192,192,192,192],
        [192,255,128,128],
        [192,255,64,64],
        [192,0,0,0]]

# question 2 b)
# partie 1
Grisbis = [[0 for i in range(8)] for j in range(10)]

# partie 2
for j in range(len(Grisbis)):
    for i in range(len(Grisbis[0])):
        Grisbis[j][i] = Gris[j//2][i//2]
# affichage
for h in range(len(Grisbis)):
    print(Grisbis[h])

print("--------------------")

# Question 4 c)
# A_prime * (A - 2 * I2)
A = [[3,1],
     [4,1]]
A_prime = [[2,-1],
           [-1,1]]
I2 = [[1,0],
      [0,1]]
B = [[0 for i in range(2)] for j in range(2)]
for j in range(len(B)):
    for i in range(len(B[0])):
        B[j][i] = A_prime[j][i] * (A[j][i] - 2 * I2[j][i])
print("Valeur du calcul A_prime * (A - 2 * I2) :")
for u in range(len(B)):
    print(B[u])

print("--------------------")

# Question 6
import statistics

image = [[0,128,255,255,200,150],
     [255,0,50,0,255,128],
     [255,255,50,0,128,150],
     [150,150,150,200,150,150],
     [128,200,50,200,150,150],
     [100,128,128,0,0,0]]
# Partie a) mode
mode = statistics.mode(image[0])
print("Mode =",mode)
# Partie b) médiane
mediane = statistics.median(image[0])
print("Mediane =",mediane)
# Partie c) moyenne et ecart type
moyenne = statistics.mean(image[0])
print("Le niveau moyen de gris =",moyenne)
ecart_type = statistics.stdev(image[0])
print("Écart-type =",ecart_type)

print("--------------------")

# Question 7
R = [[32,112,150],
      [127,21,212],
      [0,127,127]]
V = [[0,255,255],
      [0,125,127],
      [127,64,64]]
B = [[255,64,255],
     [0,64,0],
     [127,127,64]]
M = [R,V,B]
G = [[0 for i in range(len(R[0]))] for j in range(len(R))]
for j in range(len(R)):
    for i in range(len(R[0])):
        G[j][i] = 0.21*(R[j][i])+0.72*(V[j][i])+0.07*(B[j][i])
print("Transformation d'une image RVB en niveaux de gris:")
for l in range(len(G)):
    print(G[l])