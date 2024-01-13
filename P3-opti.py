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

    def creer_depuis_liste(self, elements):
        if not elements:
            return

        self.tete = Noeud(elements[0])
        current = self.tete

        for valeur in elements[1:]:
            nouveau_noeud = Noeud(valeur)
            current.suivant = nouveau_noeud
            nouveau_noeud.precedent = current
            current = nouveau_noeud

        # Fermer la boucle en reliant le dernier nœud au premier
        current.suivant = self.tete
        self.tete.precedent = current

    def avancer_ville(self):
        if self.sens:
            self.tete = self.tete.suivant
        else:
            self.tete = self.tete.precedent

    def manger_ville(self):
        # Supprimer le nœud actuel et mettre à jour les liens
        suivant = self.tete.suivant
        precedent = self.tete.precedent

        suivant.precedent = precedent
        precedent.suivant = suivant

        # Mettre à jour la tête
        self.tete = suivant

    def retourner(self):
        self.sens = not self.sens

    def recracher_ville(self):
        # Insérer un nouveau nœud devant la tête
        nouvelle_ville = Noeud(self.tete.precedent.valeur)
        nouvelle_ville.suivant = self.tete
        nouvelle_ville.precedent = self.tete.precedent

        self.tete.precedent.suivant = nouvelle_ville
        self.tete.precedent = nouvelle_ville

    def afficher_liste(self):
        current = self.tete
        while True:
            print(current.valeur)
            current = current.suivant
            if current == self.tete:
                break

def situation_finale(n: int, m: int, villes: List[str], actions: List[str]) -> None:
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

    liste_villes.afficher_liste()

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
    situation_finale(n, m, villes, actions)
