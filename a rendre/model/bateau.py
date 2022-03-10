from grille import * 
class Bateau():
    def __init__(self,id,nom,joueur,cases,status = 0):
        self.id = id
        self.nom = nom
        self.joueur = joueur
        self.cases = cases
        self.status = status
        # 0 : pas placé
        # 1 : en jeu
        # 2 : en vie
        # 3 : détruit
        self.image = None

    def touche(self,id,case,joueur):
        print("marche")

    def enVie(self):
        for case in self.cases:
            if case == 2:
                return True 
        return False
            