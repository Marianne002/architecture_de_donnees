# Ecrire un programme qui décode un message.
# Le message codé est une chaîne de nombres séparés par des espaces,
# où chaque nombre est la valeur ASCII d'un caractère.
# Votre tâche est de convertir ces nombres en la chaîne de
# caractères correspondante.


def decode_message(message):
    decoded_message = ""
    for number in message.split():
        decoded_message += chr(int(number))
    return decoded_message
