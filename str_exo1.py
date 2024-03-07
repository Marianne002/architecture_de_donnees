# EXO 1: Ecrire un programme qui accepte une chaîne de caractères
# Afficher le nb de majuscules et minuscules mais n'autorise pas les chiffres

message = "Food is the Best Thing in the World"


def count_upp_low(word):
    upper = 0
    lower = 0
    for letter in word:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return f"{upper} majuscules et {lower} minuscules"
