import random

class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        assert (c > 0 and c < 5)
        assert (v > 0 and v < 14)
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10,
       Valet, Dame, Roi"""
    def getNom(self):
        if (self.Valeur > 1 and self.Valeur < 11):
            return str(self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle)"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur-1]   # ATTENTION ! problème d'indice !

class PaquetDeCarte:
    
    
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes""" 
    def remplir(self):
        for c in range(1, 5):
            for v in range(1, 14):
                self.contenu = self.contenu + [Carte(c, v)]

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        assert pos < len(self.contenu)+1
        return self.contenu[pos-1]
    
    """Melange l'ensemble des cartes"""
    def melanger(self):
       random.shuffle(self.contenu) 
    
    """Distribue deux paquets de 26 cartes differentes aux deux joueurs"""
    def distribuer(self):
        j_1 = []
        j_2 = []
        print("__________________")
        print("Paquet du joueur 1")
        print("__________________")
        for i in range (26):
            uneCarte = unPaquet.getCarteAt(i)
            j_1.append(uneCarte.getNom() + " de " + uneCarte.getCouleur())
        print(j_1)
#         print(len(j_1))
        print("__________________")
        print("Paquet du joueur 2")
        print("__________________") 
        for i in range (26,52):
            uneCarte = unPaquet.getCarteAt(i) 
            j_2.append(uneCarte.getNom() + " de " + uneCarte.getCouleur())
        print (j_2)
#         print(len(j_2))
        print("__________________")
    # Distribution des 52 cartes aléatoires
# for i in range(52):
#     uneCarte = unPaquet.getCarteAt(i)
#     print(uneCarte.getNom() + " de " + uneCarte.getCouleur())

    """
        Permet de tirer la carte se trouvant aux sommet du paquet
        de chauque joueur
    """
#    def tirerUneCarte():



     
unPaquet = PaquetDeCarte()
unPaquet.remplir()
unPaquet.melanger()
j_1 = PaquetDeCarte()
j_2 = PaquetDeCarte()
unPaquet.distribuer()
print(type(j_1)) 
  
