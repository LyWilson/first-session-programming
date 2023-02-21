mot_de_passe = input("saisir un mot de passe acceptable")
#critere 1
if len(mot_de_passe)>=5 and len(mot_de_passe)<=10:
    c1=True
else:
    c1=False

#critere 2

min=0
maj=0
chif=0
for i in mot_de_passe:
    if i.islower():
        min = 1+min
    elif i.isupper():
        maj = 1+maj
    elif i.isnumeric():
        chif = 1+chif

if min > 0 and maj > 0 and chif > 0:
    c2 = True
else:
    c2 = False


#critere 3

if mot_de_passe[0]!=mot_de_passe[-1]:
    c3=True
else:
    c3=False

#final

if c1 and c2 and c3==True:
      print("valide")
else:
    print("non-valide")
