# Ecrire un programme qui inverse l'ordre des éléments
# dans chaque tuple d'une liste de tuples

def reverse_tuples(liste):
    return [tuple(reversed(tpl)) for tpl in liste]
