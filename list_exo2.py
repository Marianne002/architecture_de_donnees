# Ecrire un programme Python qui effectue une rotation à droite
# des éléments d'une liste.
# La rotation doit être définie par l'utilisateur.

def rotate_list(liste):
    x = input("Combien de rotation voulez-vous ? ")
    new_liste = liste[int(x):] + liste[0:int(x)]
    return new_liste
