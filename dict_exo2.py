# Gérer une base de données de produits pour un magasin en ligne,
# stockée sous forme de dictionnaire.
# Chaque clé du dictionnaire est l'identifiant du produit (un nombre entier)
# et chaque valeur est un autre dictionnaire contenant des informations
# sur le produit y compris le prix et la quantité en stock.
# Vôtre tâche est de générer une liste de produits en rupture de stock
# (quantité en stock égale à 0) triée par prix, du plus cher au moins cher.
# Si deux produits ont le même prix,
# trier-les par identifiant en ordre croissant.

def out_of_stock(products):
    rupture = [
        {"id": product, "price": infos["price"], "name": infos["name"]}
        for product, infos in products.items()
        if infos["quantity"] == 0
    ]
    return sorted(rupture, key=lambda x: (x["price"], x["id"]), reverse=True)
