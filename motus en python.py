import random


def motus():

    mots = ["python", "ordinateur", "programmation",
            "algorithmique", "développement"]

    mot_a_deviner = random.choice(mots)

    print("Bienvenue dans le jeu de Motus!")
    print("Le mot à deviner contient", len(mot_a_deviner), "lettres.")

    for tentative in range(1, 6):
        print(f"Tentative {tentative}: ")
        essai = input()

        if essai == mot_a_deviner:
            print("Bravo! Vous avez deviné le mot!")
            return

        else:
            bien_places = 0
            mal_places = 0
            for i in range(len(essai)):
                if essai[i] == mot_a_deviner[i]:
                    bien_places += 1
                elif essai[i] in mot_a_deviner:
                    mal_places += 1
            print(
                f"{bien_places} lettres bien placées et {mal_places} lettres mal placées.")

    print(f"Dommage! Le mot à deviner était {mot_a_deviner}.")


motus()
