question = ["prenom", "nom", "identifiant_unique", "note_exam1", "note_exam2", "TP1", "TP2", "ExamFinal"]
liste_eleve = []
note = []
#-------------------------------------------------------------------------
def meilleur_note():
    meilleur_note = 0
    for eleve in liste_eleve:
        if meilleur_note < eleve[8]:
            meilleur_note = eleve[8]
    return meilleur_note
#----------------------------------------------------------
def pire_note():
    pire_note = 100
    for eleve in liste_eleve:
        if pire_note > eleve[8]:
            pire_note = eleve[8]
    return pire_note
#----------------------------------------------------------
def moyenne():
    moyenne = 0
    for p in liste_eleve:
        moyenne += p[8]
    return moyenne/elevetotal
#----------------------------------------------------------
elevetotal = int(input("Saisir nombre eleve:"))
for h in range(elevetotal):
    liste_eleve.append(h)
    note.append(h)
print("------------------------")
for i in range(elevetotal):
    list1 = []
    list1.append(input("Veuillez saisir votre prenom:"))
    list1.append(input("Veuillez saisir votre nom:"))
    list1.append(input("Veuillez saisir votre identifiant:"))
    list1.append(float(input("Veuillez saisir votre note de l'exam1:")))
    list1.append(float(input("Veuillez saisir votre note de l'exam2:")))
    list1.append(float(input("Veuillez saisir votre note du TP1:")))
    list1.append(float(input("Veuillez saisir votre note du TP2:")))
    list1.append(float(input("Veuillez saisir votre note de l'exam Final:")))
    list1.append(list1[3]*0.2 + list1[4]*0.2 + list1[5]*0.15 + list1[6]*0.15 + list1[7]*0.3)
    liste_eleve[i] = list1.copy()
print(question)
for c in range(elevetotal):
    print(liste_eleve[c])

print("------------------------")
print("La moyenne de la classe:", moyenne(), "\nLa meilleur note obtenue:", meilleur_note(),"\nLe pire note obtenue:", pire_note())
