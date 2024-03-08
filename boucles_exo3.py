# Ecrire un programme qui prend trois nombres en entrée
# Et déterminer le plus grand nombre parmi eux

def higher_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
