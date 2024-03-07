# EXO2: Vous disposez de la chaîne de caractères suivante :
str = "Python est un langage de programmation puissant et facile à apprendre"


#  1.Extraire le mot "Pyhton" de la chaîne

def extract_word(word):
    return word.split()[0]


#  2. Extraire le mot "apprendre" par des indice négatifs

def extract_word_negative_index(word):
    return word.split()[-1]


#  3. Extraire la phrase "langage de programmation" en utilisant le slicing

def extract_word_slicing(word):
    return word.split()[3:6]


# Challenge: Inverser la chaîne de caractères

def reverse_string(word):
    return word[::-1]
