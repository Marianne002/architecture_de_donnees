# Etant donné un dictionnaire contenant le nom des étudiants
# et leurs notes moyennes
# Ecrire un programme qui génère un nouveau dictionnaire avec les noms
# des étudiants qui ont une note supérieure ou égale à 15.

def students_above_15(students):
    students_above_15 = {}
    for student in students:
        if students[student] >= 15:
            students_above_15[student] = students[student]
    return students_above_15
