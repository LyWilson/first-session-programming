#---------------------------------------------------------
def calcul_note_final(eleve):
  return eleve['note_exam1']*0.2 + eleve['note_exam2']*0.2 + eleve['note_tp1']*0.15 + eleve['note_tp2']*0.15 + eleve['note_exam_final']*0.3
#---------------------------------------------------------
def meilleur_note(liste_eleve):
    meilleur_note = 0
    for eleve in liste_eleve:
        if meilleur_note < eleve['note_final']:
            meilleur_note = eleve['note_final']
    return meilleur_note
#---------------------------------------------------------
def pire_note(liste_eleve):
    pire_note = 100
    for eleve in liste_eleve:
        if pire_note > eleve['note_final']:
            pire_note = eleve['note_final']
    return pire_note
#---------------------------------------------------------
def moyenne(liste_eleve):
    moyenne = 0
    for eleve in liste_eleve:
        moyenne += eleve['note_final']
    return moyenne/elevetotal
#---------------------------------------------------------
liste_eleve = []
elevetotal = int(input("Saisir nombre eleve:"))
print("------------------------")
for i in range(elevetotal):
    eleve = {}
    eleve['prenom'] = input("Veuillez saisir votre prenom:")
    eleve['nom'] = input("Veuillez saisir votre nom:")
    eleve['identifiant'] = input("Veuillez saisir votre identifiant:")
    eleve['note_exam1'] = float(input("Veuillez saisir votre note de l'exam1:"))
    eleve['note_exam2'] = float(input("Veuillez saisir votre note de l'exam2:"))
    eleve['note_tp1'] = float(input("Veuillez saisir votre note du TP1:"))
    eleve['note_tp2'] = float(input("Veuillez saisir votre note du TP2:"))
    eleve['note_exam_final'] = float(input("Veuillez saisir votre note de l'exam Final:"))
    eleve['note_final'] = calcul_note_final(eleve)
    liste_eleve.append(eleve)
print("------------------------")
for eleve in liste_eleve:
    print(eleve)
print("------------------------")
print("la moyenne de la classe:", moyenne(liste_eleve), "\nmeilleur note obtenue:", meilleur_note(liste_eleve), "\npire note obtenue:", pire_note(liste_eleve))