nb1 = input("entrez premier nombre")
nb2 = input("entrez deuxieme nombre")
nb3 = input("entrez troisieme nombre")
if nb1 < nb2 and nb2<nb3:
    print("en ordre croissant")
else:
    print("en desordre")


nb4 = input("entrez premier nombre")
nb5 = input("entrez deuxieme nombre")
nb6 = input("entrez troisieme nombre")
if nb4<nb5:
    if nb5<nb6:
        print("en ordre croissant")
    else:
        print("en desordre")