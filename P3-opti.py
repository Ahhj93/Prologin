N: int = int(input()) # Nombre de villes
M: int = int(input()) # Nombre d'années avant le Ragnarök
villes: list = [] # Liste des villes
for i in range(N):
    villes.append(input())
actions: list = [elt for elt in input()] # Liste des actions

ventre: list = [] # Liste des villes mangées
indice_ventre: int = 0 # Indice de la ville mangée actuelle

indice: int = 0 # Indice de la ville actuelle
avant: bool = True # True si le serpent avance de gauche à droite, False sinon

# Afficher liste de villes depuis l'indice
def affiche(liste: list, indice: int, avant: bool):
    liste: list = villes[indice:] + villes[:indice]
    if not avant:
        liste = liste[::-1]
    for ville in liste:
        print(ville)

for action in actions:
    if action == "A":
        # Avancer d'une ville de manière circulaire dans la liste
        if avant:
            indice = (indice + 1) % N
        else:
            indice = (indice - 1) % N
    elif action == "M":
        # Manger la ville la plus proche devant sa tête
        N -= 1
        if avant:
            ventre.append(villes.pop(indice))
            indice = indice % N
        else:
            ventre.append(villes.pop(indice-1))
            indice = (indice - 1) % N
    elif action == "R":
        # Se retourner, ce qui signifie qu'il avancera alors dans
        # la direction opposée par la suite. S'il avançait de gauche à droite,
        # il avance alors de droite à gauche, et inversement
        avant = not avant
    elif action == "C":
        # Recracher la dernière ville qu'il a mangé et qu'il n'a pas encore recraché,
        # pour la placer devant sa tête
        N += 1
        if avant:
            villes.insert(indice, ventre.pop(len(ventre)-1))
        else:
            villes.insert(indice, ventre.pop(len(ventre)-1))
            indice = (indice + 1) % N

# On affiche les villes à partir de l'indice
affiche(villes, indice, avant)