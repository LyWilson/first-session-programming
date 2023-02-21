def longueurEntier (unNbre):
    nbChiffres = 1
    base = 10
    while((unNbre/base) >= 1) :
        nbChiffres=nbChiffres + 1
        base=base * 10
    return nbChiffres

unNbre=float(input("saisir un nombre"))

#cette fonction permet de calculer la longueur du nombre entier par exemple 1000 c'est 4