from typing import List
import sys

def afficher_chemin(n: int, dieux: List[str]) -> None:
    """
    :param n: le nombre de dieux
    :param dieux: liste des prénoms et noms des dieux séparés par un espace
    """
    # S'il n'existe aucun chemin qui permette de faire passer le message
    # par tous les dieux en respectant le protocole HTTP, afficher sur une
    # ligne le message `IMPOSSIBLE`. Sinon, afficher, sur une ligne par dieu et
    # dans l'ordre désiré, les noms complets des dieux par lesquels le message
    # doit passer. Si plusieurs solutions existent, afficher n'importe laquelle
    # d'entre elles.

    def est_transfert_valide(dieu_precedent: str, dieu_actuel: str, meme_type: bool) -> bool:
        """
        :param dieu_precedent: le nom du dieu précédent
        :param dieu_actuel: le nom du dieu actuel
        :param meme_type: True si le dieu précédent et le dieu actuel sont de même type, False sinon
        """
        # Vérifiez si le transfert du message entre le dieu précédent et le dieu actuel est valide
        prenom_precedent, nom_precedent = dieu_precedent.split()
        prenom_actuel, nom_actuel = dieu_actuel.split()

        if meme_type:
            return prenom_precedent == prenom_actuel
        else:
            return nom_precedent == nom_actuel
        
    def parcours_chemin(chemin: List[str], meme_type: bool):
        """
        :param chemin: le chemin actuel
        :param meme_type: True si le dieu précédent et le dieu actuel sont de même type, False sinon
        """
        # Essaye de trouver un chemin valide
        if len(chemin) == n:
            # Tous les dieux ont reçu le message
            print('\n'.join(chemin))
            sys.exit(0)

        for dieu in dieux:
            if dieu not in chemin and est_transfert_valide(chemin[-1], dieu, meme_type):
                chemin.append(dieu)
                parcours_chemin(chemin, not meme_type)
                chemin.pop()

    for i in range(n):
        # Démarre le parcours à partir de chaque dieu
        parcours_chemin([dieux[i]], True)
        parcours_chemin([dieux[i]], False)

    # Si aucune solution n'est trouvée
    print("IMPOSSIBLE")

if __name__ == "__main__":
    n = int(input())
    dieux = [input() for _ in range(n)]
    afficher_chemin(n, dieux)
