from typing import List


def chemin_valide(n: int, dieux: List[str], m: int, passations: List[str]) -> None:
    """
    Vérifie si les transmissions du message respectent le protocole HTTP.
    :param n: le nombre de dieux
    :param dieux: liste des prénoms et noms des dieux séparés par un espace
    :param m: nombre de passations du message
    :param passations: liste des échanges de message entre les dieux, les noms complets des deux dieux séparés par un espace
    """
    transmissions = set(passations)  # Convertit la liste des transmissions en ensemble pour une recherche plus rapide
    possible_dieux_initiaux = []

    # Parcourt tous les dieux pour les considérer comme dieu initial
    for dieu_initial in dieux:
        chemin = [dieu_initial]  # Initialise le chemin avec le dieu initial
        dernier_dieu = dieu_initial

        # Effectue les transmissions suivant les règles du protocole HTTP
        for _ in range(n - 1):
            transmission_possible = False

            # Parcourt tous les dieux pour trouver le prochain destinataire possible
            for dieu in dieux:
                transmission = f"{dernier_dieu} {dieu}"

                if transmission in transmissions and dieu not in chemin and all(
                    f"{dieu2} {dieu}" not in transmissions for dieu2 in chemin
                ):
                    chemin.append(dieu)
                    dernier_dieu = dieu
                    transmission_possible = True
                    break

            # Si aucune transmission possible, abandonne le chemin
            if not transmission_possible:
                break

        # Vérifie si le chemin a atteint tous les dieux
        if len(set(chemin)) == n:
            possible_dieux_initiaux.append(dieu_initial)

    # Affiche le résultat
    if possible_dieux_initiaux:
        print("OUI")
        for dieu_initial in possible_dieux_initiaux:
            print(dieu_initial)
    else:
        print("NON")


if __name__ == "__main__":
    n = int(input())
    dieux = [input() for _ in range(n)]
    m = int(input())
    passations = [input() for _ in range(m)]
    chemin_valide(n, dieux, m, passations)
