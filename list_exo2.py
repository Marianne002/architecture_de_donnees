# Ecrire un programme Python qui effectue une rotation à droite
# des éléments d'une liste.
# La rotation doit être définie par l'utilisateur.

def rotate_list(input_list, rotation):
    return input_list[-rotation:] + input_list[:-rotation]
