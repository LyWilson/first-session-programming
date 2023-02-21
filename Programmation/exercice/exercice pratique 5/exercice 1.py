a = "DEC"
b = "informatique"
c = 25
d = "40"


# commande                           valide                             affichage si oui sinon correction
# len(a)                             valide                             3
print(len(a))

# len(a+b)                           valide                             15
print(len(a+b))

# len(a+""+b)                        valide                             16
print(len(a+" "+b))

# len(a+"\t"+b)                      valide                             16
print(len(a+"\t"+b))

# a+b                                valide                             DECinformatique
print(a+b)

# a+" en "+b                         valide                             DEC en informatique
print(a+" en "+b)

# a[1:2]                             valide                             E
print(a[1:2])

# b[:4]                              valide                             info
print(b[:4])

# b[5:15]                            valide                             matique
print(b[5:15])

# c+1                                valide                             26
print(c+1)

# c+"1"                              invalide                           print(str(c)+"1")
print(str(c)+"1")
# correcte forme sinon erreur print(c+"1") pas bon car 1 est str et non int
# forme incorrecte --> print(c+"1")

# d+1                                invalide                           print(int(d)+1)
print(int(d) + 1)
# correcte forme sinon erreur print(d+1) pas bon car 1 est int et non str
# forme incorrecte --> print(d+1)

# d+"1"                               valide                              401
print(d+"1")

# c * 2                               valide                              50
print(c*2)

# d * 2                               valide                              4040
print(d*2)