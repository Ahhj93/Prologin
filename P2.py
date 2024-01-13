from typing import List

def ordre(k: int, n: int, tailles: List[int]) -> None:
    """
    :param k: le nombre magique
    :param n: le nombre de personnes
    :param tailles: la liste des tailles de chaque personne
    """
    # Afficher **OUI** s'il est possible de trier les personnes par taille
    # ou **NON** si ce n'est pas possible.
    for i in range(k):
        # Extraire les sous-listes associées à chaque classe d'équivalence modulo K
        sous_liste = tailles[i::k]
        # Trier chaque sous-liste
        sous_liste.sort()

        # Remettre les sous-listes triées à leur place dans la liste originale
        tailles[i::k] = sous_liste

    # Vérifier si la liste entière est triée après avoir traité toutes les sous-listes
    est_triee = all(tailles[i] <= tailles[i + 1] for i in range(n - 1))

    return "OUI" if est_triee else "NON"


if __name__ == "__main__":
    k = int(input())
    n = int(input())
    tailles = list(map(int, input().split()))
    print(ordre(k, n, tailles))