import math
aire=0
def surfCercle(R):
    aire=R*R*math.pi
    print(aire)

R=float(input("saisir le rayon"))
surfCercle(R)