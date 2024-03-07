# Ecrire un programme Python qui prend une liste de tuples
# Afficher le tuple avec le plus d'éléments

def tuple_max(liste):
    if liste == []:
        return None
    else:
        return max(liste, key=len)
