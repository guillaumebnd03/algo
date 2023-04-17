import random


def obtenir_mot_aleatoire(nom_fichier):
    with open(nom_fichier, "r") as f:
        mots = f.readlines()
    return random.choice(mots).strip()


def afficher_score(score):
    print(f"Votre score actuel est {score}.")


def motus():
    fichier_mots = "mots.txt"
    mots = [mot.upper() for mot in obtenir_mot_aleatoire(fichier_mots)]
    mot_a_deviner = random.choice(mots)

    print("Bienvenue dans le jeu de Motus!")
    print(f"Il y a {len(mots)} mots dans le fichier {fichier_mots}.")
    print("Le mot à deviner contient", len(mot_a_deviner), "lettres.")
    score = 0

    while True:
        print("Nouvelle tentative:")
        essai = input().strip().upper()

        if essai == mot_a_deviner:
            score += 10
            print("Bravo! Vous avez deviné le mot!")
            afficher_score(score)
            print("Voulez-vous rejouer? (o/n)")
            choix = input().lower()
            if choix == "o":
                mot_a_deviner = random.choice(mots)
                print("Le nouveau mot à deviner contient",
                      len(mot_a_deviner), "lettres.")
            else:
                print("Merci d'avoir joué!")
                return

        else:
            bien_places = 0
            mal_places = 0
            for i in range(len(essai)):
                if essai[i] == mot_a_deviner[i]:
                    bien_places += 1
                elif essai[i] in mot_a_deviner:
                    mal_places += 1
            score -= 1
            print(
                f"{bien_places} lettre(s) bien placée(s) et {mal_places} lettre(s) mal placée(s).")
            afficher_score(score)

            if score < -5:
                print("Vous avez perdu!")
                print(f"Le mot à deviner était {mot_a_deviner}.")
                print("Voulez-vous rejouer? (o/n)")
                choix = input().lower()
                if choix == "o":
                    mot_a_deviner = random.choice(mots)
                    print("Le nouveau mot à deviner contient",
                          len(mot_a_deviner), "lettres.")
                    score = 0
                else:
                    print("Merci d'avoir joué!")
                    return

            elif score >= 20 and len(mots) > 1:
                print("Félicitations, vous avez débloqué un nouveau mot!")
                mots.remove(mot_a_deviner)
                mot_a_deviner = random.choice(mots)
                print("Le nouveau mot à deviner contient",
                      len(mot_a_deviner), "lettres.")
                afficher_score(score)


motus()
