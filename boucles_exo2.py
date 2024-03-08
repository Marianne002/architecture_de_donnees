# Écrire un programme qui affiche une pyramide d'étoiles (*).
# L'utilisateur doit indiquer la hauteur de la pyramide
# Et le programme génère la pyramide correspondante.

def show_pyramide():
    hauteur = int(input("Entrez la hauteur de la pyramide : "))
    for i in range(1, hauteur + 1):
        print(" " * (hauteur - i) + "*" * (2 * i - 1))


show_pyramide()
