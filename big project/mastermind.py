import random

def generate_secret_code():
    secret_code = []
    for i in range(4):
        secret_code.append(random.randint(0, 9))
    return secret_code

def check_guess(guess, secret_code):
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(4):
        if guess[i] == secret_code[i]:
            correct_digits_and_position += 1
        elif guess[i] in secret_code:
            correct_digits_only += 1
    return correct_digits_and_position, correct_digits_only

def play_game():
    secret_code = generate_secret_code()
    num_guesses = 0
    while num_guesses < 10:
        guess = input("4 chiffres rentrer tu dois: ")
        guess = [int(x) for x in guess]
        correct_digits_and_position, correct_digits_only = check_guess(guess, secret_code)
        print("Correcte tes chiffres et positions sont: ", correct_digits_and_position)
        print("Seul correct ton chiffres est: ", correct_digits_only)
        num_guesses += 1
        if correct_digits_and_position == 4:
            print("Bravo, la combinaison mystère trouver tu as!")
            return
    print("Désolé, mais nul tu est", secret_code)

play_game()