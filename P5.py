from typing import List
import sys
sys.setrecursionlimit(10000000)

def chemin_valide(n: int, dieux: List[str], m: int, passations: List[str]) -> None:
    """
    :param n: le nombre de dieux
    :param dieux: liste des prénoms et noms des dieux séparés par un espace
    :param m: nombre de passations du message
    :param passations: liste des échanges de message entre les dieux, les noms complets des deux dieux séparés par un espace
    """
    def est_bonne_racine(racine, voisins_arbre):
        # Initialisation des ensembles et dictionnaires pour le suivi des dieux visités
        premiers_mauvais: set = set()
        derniers_mauvais: set = set()
        visites: dict = {dieu: False for dieu in voisins_arbre}

        def rec_aux(dieu, ancetre):
            # Fonction récursive pour explorer les voisins de chaque dieu dans l'arbre
            prenom, nom = dieu
            if prenom in premiers_mauvais or nom in derniers_mauvais or visites[dieu]:
                return False
            else:
                visites[dieu] = True
                for voisin in voisins_arbre[dieu] - {ancetre}:
                    if not rec_aux(voisin, dieu):
                        return False
                premiers_mauvais.add(prenom)
                derniers_mauvais.add(nom)
                return True
            
        # Appel de la fonction récursive pour vérifier si la racine est bonne
        if rec_aux(racine, ("PasPossible", "IlsOntCela")):
            if all(visites[dieu] for dieu in voisins_arbre):
                return True
        return False
    
    # Vérification du nombre de dieux et passations
    if n != (m + 1):
        print("NON")
        return

    # Création d'un dictionnaire pour enregistrer les voisins dans l'arbre pour chaque dieu
    voisins_dans_arbre: dict = {tuple(dieu.split()): set() for dieu in dieux}

    # Analyse des passations pour construire l'arbre des voisins
    for dieux_echange in passations:
        dieux_propres = dieux_echange.split()
        dieu1 = tuple(dieux_propres[:2])
        dieu2 = tuple(dieux_propres[2:])
        if dieu1[1] != dieu2[1] and dieu1[0] != dieu2[0]:
            print("NON")
            return
        voisins_dans_arbre[dieu1].add(dieu2)
        voisins_dans_arbre[dieu2].add(dieu1)

    # Recherche des bonnes racines dans l'arbre
    bonnes_racines: list = [racine for racine in voisins_dans_arbre if est_bonne_racine(racine, voisins_dans_arbre)]

    # Affichage du résultat
    if bonnes_racines:
        print("OUI")
        print("\n".join(" ".join(dieu) for dieu in bonnes_racines))
    else:
        print("NON")

if __name__ == "__main__":
    n = int(input())
    dieux = [input() for _ in range(n)]
    m = int(input())
    passations = [input() for _ in range(m)]
    chemin_valide(n, dieux, m, passations)
