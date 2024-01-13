from typing import List

def situation_finale(n: int, m: int, villes: List[str], actions: List[str]) -> None:
    """
    :param n: le nombre de villes autour de Midgard
    :param m: le nombre d'années avant le Ragnarök
    :param villes: le nom des villes autour de Midgard, en partant de la queue de Jörmungandr

    :param actions: la liste des actions prochaines de Jörmungandr
    """
    # TODO Afficher, sur une ligne par ville, la liste des villes qui seront
    # rencontrées lors du Ragnarök, dans l'ordre, en partant de la queue de
    # Jörmungandr jusqu'à sa tête.
    ventre: list = [] # Liste des villes mangées
    indice_ventre: int = 0 # Indice de la ville mangée actuelle

    indice: int = 0 # Indice de la ville actuelle

    tmp: list = villes[:]
    sens: bool = True # True: de gauche à droite, False: de droite à gauche

    nb_villes: int = n

    for action in actions:
        if action == "A":
            # Avancer d'une ville de manière circulaire dans la liste
            if sens:
                indice += 1
            else:
                indice -= 1
            indice %= nb_villes
        elif action == "M":
            # Manger la ville la plus proche devant sa tête
            if sens:
                ventre.append(tmp.pop(indice))
            else:
                ventre.append(tmp.pop(indice-1))
                if indice != 0:
                    indice -= 1
            nb_villes -= 1
            indice %= nb_villes
        elif action == "R":
            # Se retourner, ce qui signifie qu'il avancera alors dans
            # la direction opposée par la suite. S'il avançait de gauche à droite,
            # il avance alors de droite à gauche, et inversement
            sens = not sens
        elif action == "C":
            # Recracher la dernière ville qu'il a mangé et qu'il n'a pas encore recraché,
            # pour la placer devant sa tête
            if sens:
                tmp.insert(indice, ventre.pop(len(ventre)-1))
            else:
                tmp.insert(indice, ventre.pop(len(ventre)-1))
                indice += 1
            nb_villes += 1
            indice %= nb_villes
        #print(action, indice, end=" ")
        #affiche_villes(sens, indice, tmp)
    affiche_villes(sens, indice, tmp)

def affiche_villes(sens, indice, villes):
    if sens:
        #print(*villes[indice:] + villes[:indice])
        print(*villes[indice:] + villes[:indice], sep="\n")
    else:
        #print(*(villes[indice:] + villes[:indice])[::-1])
        print(*(villes[indice:] + villes[:indice])[::-1], sep="\n")

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
    situation_finale(n, m, villes, actions)
