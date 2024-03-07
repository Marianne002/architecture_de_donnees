# Écrire un programme Python qui prend une liste
# Retourner une nouvelle liste contenant uniquement
# les éléments uniques de la 1ere liste

def filter_unique_elements(input_list):
    unique_elements = []
    for item in input_list:
        if input_list.count(item) == 1:
            unique_elements.append(item)
    return unique_elements
