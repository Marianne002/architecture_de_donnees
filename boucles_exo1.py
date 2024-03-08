# Écrire un programme qui choisit un nombre aléatoire entre 1 et 100
# Demander à l'utilisateur de le deviner.
# L'utilisateur a droit à un nombre limité de tentatives.
# Après chaque tentative, le programme indique si le nombre mystère est
# plus grand ou plus petit que la saisie de l'utilisateur.

import random


def guess_number():
    mystery_number = random.randint(1, 100)
    remaining_attempts = 10
    print("Devinez le nombre mystère entre 1 et 100.")

    while remaining_attempts > 0:
        try:
            guess = int(input("Votre proposition : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if guess == mystery_number:
            print(f"Vous avez trouvé le nombre mystère : {mystery_number}")
            break
        elif guess < mystery_number:
            print("Le nombre mystère est plus grand.")
        else:
            print("Le nombre mystère est plus petit.")

        remaining_attempts -= 1
        print(f"Tentatives restantes : {remaining_attempts}")

    if remaining_attempts == 0:
        print(f"Dommage. Le nombre mystère était : {mystery_number}")
    return mystery_number
