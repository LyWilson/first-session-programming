nb1=int(input("un premier nombre"))
operateur=input("un operateur arithmétique (+, -, * ou /)")
nb2=int(input("un deuxieme nombre"))
rep=float(input("votre reponse"))
i=0
if operateur == "+":
    reponse = nb1 + nb2
elif operateur == "-":
    reponse = nb1 - nb2
elif operateur == "*":
    reponse = nb1 * nb2
elif operateur == "/":
    reponse = nb1 / nb2
else:
    print("mauvaise operateur")
print(reponse)
if reponse == rep:
    print("Bravo!")

else:
    while i<=8:
        rep=float(input("saisir votre reponse"))
        if rep!=reponse:
            i+=1
            print("reessaye")
        else:
            i+=10
            print("Bravo")
    print("raté")