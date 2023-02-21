from random import*

#question 1
a=randint(1,30)

for i in range(100):
    print(i,a)
    if a == 1:
        print("atterrissage !")
        break
    else:
        if (a%2) == 0:
            a=a//2
        else:
            a=(3*a)+1
    
#question 2

a=int(input("saisir un chiffre entre 1 et 30 "))
for i in range(100):
    print(i,a)
    if a == 1:
        print("atterrissage !")
        break
    else:
        if (a%2) == 0:
            a=a//2
        else:
            a=(3*a)+1

#question 3 Bonus

a=int(input("saisir un chiffre entre 1 et 30 "))
compteur=1
for i in range(1,30):
    print(i,a)
    if a == 1:
        print("nombre d'itérations= ",compteur)
        print("atterrissage !")
        break
    else:
        if (a%2) == 0:
            a=a//2
            compteur+=1
        else:
            a=(3*a)+1
            compteur+=1
