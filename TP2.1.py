# Variable/ initialisation de la liste
list_article = []

# Fonction d'article nontaxable
def nontaxable():
    article = {"nom": input("Saisir le nom de l'article : "),
               "prix unitaire": float(input("Saisir le prix de l'article : ").replace(",", ".")),
               "quantite": int(input("Saisir la quantite de l'article : "))}
    # ici la fonction "replace" convertir un chiffre à virgule avec un point pour éviter une erreur
    article["prix total"] = article["prix unitaire"] * article["quantite"]
    # on utilise des dictionnaires dans les listes pour simplifier la recherche des articles dans la liste
    list_article.append(article)


# Fonction d'article taxable
def taxable():
    article = {"nom": input("Saisir le nom de l'article : "),
               "prix unitaire": float(input("Saisir le prix de l'article : ").replace(",", ".")),
               "quantite": int(input("Saisir la quantite de l'article : "))}
    article["prix total"] = (article["prix unitaire"] * article["quantite"]) + 0.14975 * (article["prix unitaire"] * article["quantite"])
    list_article.append(article)


# Fonction supprimer un article du panier
def supprimer():
    supp_article = input("Saisir le nom de l'article a supprimer : ")
    for k in range(len(list_article)):
        # on utilise la fonction len pour parcourir la liste et si l'article est = à celui entré on le supprime
        if supp_article == list_article[k]["nom"]:
            list_article.pop(k)
            print("Article supprimé")
            break
        elif k == len(list_article) - 1:
            # il faut mettre cette condition pour éviter que "article introuvable" ne se répète pas plusieur fois
            print("Article introuvable.")


# Fontion création de facture et quitté (matière jamais vue, alors plus de commentaire)
def facture():
    montant_total = 0
    for k in range(len(list_article)):
        montant_total += list_article[k]["prix total"]
    print("\nVotre reçu : ", "\n#############")
    # Afficher titres des colonnes
    print("%-20s | %8s | %10s | %10s" % ("Articles", "Prix unité", "Quantité", "Prix total"))
    # """Dans cette ligne de code on utilise le % pour alligner les colonnes et les espaces
    # (ex: %-20s) indique que la première colonne aura 20 espaces/caractère et sera aligné à gauche"""
    print("-" * 60)
    # afficher les articles, prix, quantité et total pour chaque article dans les colonnes appropriées
    for achat in range(len(list_article)):
        article = list_article[achat]["nom"]
        prix = list_article[achat]["prix unitaire"]
        quantite = list_article[achat]["quantite"]
        prix_total = list_article[achat]["prix total"]
        print("%-20s | %10.2f | %10d | %10.2f" % (article, prix, quantite, prix_total))
    # Afficher le total
    print("-" * 60)
    print("Total : %51.2f" % montant_total)
    quit()
    # la fonction "quit" permet de quitter la boucle du menu et afficher la facture de tous les articles


# Menu
caissier = input("Quel est le prénom du caissier(ère) : ")
print("Bonjour", caissier, "bon courage en cette journée de travail !")
while True:
    print("\nMenu", "\n##########", "\n\t1- Ajouter un article non-taxable", "\n\t2- Ajouter un article taxable",
          "\n\t3- Supprimer un article de la liste d'achats", "\n\t4- Générer la facture et Quitter")
    choix = input("Veuillez choisir l'un des options suivants : ")
    # ici pas de "int" car on veut que le programme continue sans de erreur et falloir redémarré le programme si on met une lettre
    if choix == "1":
        nontaxable()
    elif choix == "2":
        taxable()
    elif choix == "3":
        supprimer()
    elif choix == "4":
        facture()
    else:
        print("Erreur")
