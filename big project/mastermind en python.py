import random


def generate_secret_code(length, range_start, range_end):
    secret_code = []
    for i in range(length):
        secret_code.append(random.randint(range_start, range_end))
    return secret_code


def check_guess(guess, secret_code):
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(guess)):
        if guess[i] == secret_code[i]:
            correct_digits_and_position += 1
        elif guess[i] in secret_code:
            correct_digits_only += 1
    return correct_digits_and_position, correct_digits_only


def play_game():
    print("Bienvenue au jeu Mastermind!")
    while True:
        length = int(input("Longueur de la combinaison mystère: "))
        range_start = int(input("Début de la plage de chiffres: "))
        range_end = int(input("Fin de la plage de chiffres: "))
        max_attempts = int(input("Nombre maximum d'essais: "))

        secret_code = generate_secret_code(length, range_start, range_end)
        num_guesses = 0
        while num_guesses < max_attempts:
            guess = input(
                f"{length} chiffres entre {range_start} et {range_end} tu dois rentrer: ")
            guess = [int(x) for x in guess]
            correct_digits_and_position, correct_digits_only = check_guess(
                guess, secret_code)
            print("Tes chiffres sont bon et bien placés ",
                  correct_digits_and_position)
            print("Tes chiffres sont bon mais mal placés ", correct_digits_only)
            num_guesses += 1
            if correct_digits_and_position == length:
                score = max_attempts - num_guesses + 1
                print("Tu as trouver la combinaision mystère!")
                print("Ton score est:", score)
                replay = input("Voulez-vous rejouer? (o/n) ")
                if replay.lower() == "o":
                    break
                else:
                    print("Merci d'avoir joué!")
                    return

        if num_guesses == max_attempts:
            print("Nul La combinaison mystère était", secret_code)
            replay = input("Voulez-vous rejouer? (o/n) ")
            if replay.lower() == "o":
                continue
            else:
                print("Merci d'avoir joué!")
                return


play_game()
