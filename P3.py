N: int = int(input()) # Nombre de villes
M: int = int(input()) # Nombre d'années avant le Ragnarök
villes: list = [] # Liste des villes
for i in range(N):
    villes.append(input())
actions: list = [elt for elt in input()] # Liste des actions

ventre: list = [] # Liste des villes mangées
indice_ventre: int = 0 # Indice de la ville mangée actuelle

for action in actions:
    if action == "A":
        # Avancer d'une ville de manière circulaire dans la liste
        villes = villes[1:] + villes[:1]
    elif action == "M":
        # Manger la ville la plus proche devant sa tête
        ventre.append(villes.pop(0))
    elif action == "R":
        # Se retourner, ce qui signifie qu'il avancera alors dans
        # la direction opposée par la suite. S'il avançait de gauche à droite,
        # il avance alors de droite à gauche, et inversement
        villes = villes[::-1]
    elif action == "C":
        # Recracher la dernière ville qu'il a mangé et qu'il n'a pas encore recraché,
        # pour la placer devant sa tête
        villes.insert(0, ventre.pop(len(ventre)-1))
    print(villes)

# On affiche les villes
for ville in villes:
    print(ville)