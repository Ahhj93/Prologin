from typing import List

def max_villes(n: int, k: int, villes: List[int], indice: int):
    """
    :param n: le nombre de villes
    :param k: le nombre de villes impliquées dans chaque mouvement
    :param villes: le nombre de bâtiments cassés dans chaque ville
    :param indice: indice de la ville de départ
    :return: maximum des villes parcourues
    """
    tmp: list = []
    if indice+k <= len(villes):
        tmp = villes[indice:indice+k]
    else:
        tmp = villes[indice:] + villes[:indice+k-len(villes)]
    return max(tmp)

def batiments(n: int, r: int, k: int, villes: List[int]) -> None:
    """
    :param n: le nombre de villes
    :param r: le nombre de mouvements du serpent
    :param k: le nombre de villes impliquées dans chaque mouvement
    :param villes: le nombre de bâtiments cassés dans chaque ville
    """
    # Afficher le nombre de bâtiments cassés à chaque ville après les $R$
    # mouvements sous la forme d'une suite d'entiers séparés par des espaces.
    tmp: list = villes[:]
    for i in range(r):
        tmp[i%n] = max_villes(n, k, tmp, i%n)
    print(*tmp)

if __name__ == "__main__":
    n = int(input())
    r = int(input())
    k = int(input())
    villes = list(map(int, input().split()))
    batiments(n, r, k, villes)
