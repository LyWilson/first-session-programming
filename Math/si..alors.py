a=37
if a >= 0:
    print("Le nombre est positif.")
else:
    print("Le nombre est négatif.")

print("-----------------------")

prenom = input("Comment t'appelles-tu ? ")
print("Bonjour",prenom)

age_chaine = input("Quel âge as-tu ? ")
age = int(age_chaine)

if age >= 18:
    print("Tu es majeur !")
else:
    print("Tu es mineur !")

print("-----------------------")

from random import*
a = randint(1,12)
print("a=",a)
b = randint(1,12)
print("b=",b)

reponse = int(input("Combien vaut le produit a × b ?"))

if reponse == (a*b):
    print("Bravo!")
else:
    print("Perdu ! La bonne réponse était ", a*b)

print("-----------------------")

compteur=0
for d in range(10):
    for c in range(10):
        for u in range(10):
            if u==3:
                if d+c+u>=15:
                    if c%2==0:
                        n = 100*d+10*c + u
                        compteur+=1
                        print(n)
print("compteur= ",compteur)
                        


