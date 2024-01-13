from typing import List

class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.precedent = None
        self.suivant = None

class Liste_doublement_chainee:
    def __init__(self):
        self.tete = None
        self.sens = True
        self.mangees = []

    def creer_depuis_liste(self, elements):
        """
        Crée une liste doublement chaînée à partir d'une liste Python.
        """
        if not elements:
            return

        # Création du premier nœud
        self.tete = Noeud(elements[0])
        current = self.tete

        # Ajout des nœuds suivants à partir de la liste
        for valeur in elements[1:]:
            nouveau_noeud = Noeud(valeur)
            current.suivant = nouveau_noeud
            nouveau_noeud.precedent = current
            current = nouveau_noeud

    def avancer_ville(self):
        if self.sens:
            self.tete = self.tete.suivant
        else:
            self.tete = self.tete.precedent

    def manger_ville(self):
        ville_mangee = self.tete.suivant if self.sens else self.tete.precedent
        self.mangees.append(ville_mangee.valeur)
        self.tete = ville_mangee.suivant if self.sens else ville_mangee.precedent
        ville_mangee.precedent = None
        ville_mangee.suivant = None

    def retourner(self):
        self.sens = not self.sens

    def recracher_ville(self):
        if self.mangees:
            ville_recrachee = Noeud(self.mangees.pop())
            if self.sens:
                ville_recrachee.suivant = self.tete
                ville_recrachee.precedent = self.tete.precedent
                self.tete.precedent = ville_recrachee
            else:
                ville_recrachee.precedent = self.tete
                ville_recrachee.suivant = self.tete.suivant
                self.tete.suivant = ville_recrachee

    def ajouter_ville(self, valeur):
        nouveau_noeud = Noeud(valeur)
        if self.tete is None:
            self.tete = nouveau_noeud
        else:
            dernier_noeud = self.tete.precedent
            dernier_noeud.suivant = nouveau_noeud
            nouveau_noeud.precedent = dernier_noeud
            nouveau_noeud.suivant = self.tete
            self.tete.precedent = nouveau_noeud


def situation_finale(n: int, m: int, villes: List[str], actions: List[str]) -> None:
    """
    :param n: le nombre de villes autour de Midgard
    :param m: le nombre d'années avant le Ragnarök
    :param villes: le nom des villes autour de Midgard, en partant de la queue de Jörmungandr
    :param actions: la liste des actions prochaines de Jörmungandr
    """
    liste_villes = Liste_doublement_chainee()
    liste_villes.creer_depuis_liste(villes)

    for action in actions:
        if action == 'A':
            liste_villes.avancer_ville()
        elif action == 'M':
            liste_villes.manger_ville()
        elif action == 'R':
            liste_villes.retourner()
        elif action == 'C':
            liste_villes.recracher_ville()

    # Afficher le résultat dans l'ordre de la queue à la tête
    current = liste_villes.tete
    for _ in range(n):
        print(current.valeur)
        current = current.suivant


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
    situation_finale(n, m, villes, actions)
