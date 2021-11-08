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
    
#     """Distribue deux paquets de 26 cartes differentes aux deux joueurs"""
#     def distribuer(self):
# #         self.j_1 = [] #crée liste joueur 1
# #         self.j_2 = [] #crée liste joueur 2
#         print("__________________")
#         print("Paquet du joueur 1")
#         print("__________________")
#         for i in range (26):
#             uneCarte = unPaquet.getCarteAt(i)
#             self.j_1.append(uneCarte.getNom() + " de " + uneCarte.getCouleur())
#         print(self.j_1)
# #         print(len(j_1))
#         print("__________________")
#         print("Paquet du joueur 2")
#         print("__________________") 
#         for i in range (26,52):
#             uneCarte = unPaquet.getCarteAt(i) 
#             self.j_2.append(uneCarte.getNom() + " de " + uneCarte.getCouleur())
#         print(self.j_2)
# #         print(len(j_2))
#         print("__________________")
#     # Distribution des 52 cartes aléatoires
# # for i in range(52):
# #     uneCarte = unPaquet.getCarteAt(i)
# #     print(uneCarte.getNom() + " de " + uneCarte.getCouleur())

    """
        Permet de tirer la carte se trouvant aux sommet du paquet
        de chaque joueur
    """
    def tirerUneCarte(self):
#         for i in range(1, 27):
            carte = self.contenu[-1]
            self.contenu.pop()
            return carte
#         for i in range(27, 53):
#             j_2 = self.contenu[-1]
#             self.contenu.pop()
#         return j_2

    def ajouterCarte(self, carte):
        self.contenu.append(carte)
        
    def estVide(self):
        return (self.contenu == [])

    def taille(self):
        return len(self.contenu)
        
     
unPaquet = PaquetDeCarte()
unPaquet.remplir()
unPaquet.melanger()
j_1 = PaquetDeCarte()
j_2 = PaquetDeCarte()
temp = PaquetDeCarte()
for i in range(0, 26):
    carte = unPaquet.tirerUneCarte()
    j_1.ajouterCarte(carte)
    
for i in range(0, 26):
    carte = unPaquet.tirerUneCarte()
    j_2.ajouterCarte(carte)
    
# print(j_1.taille())
# print(j_2.taille())

# for i in range(26):    
#     uneCarte = j_1.getCarteAt(i)
#     print("j1 : " + uneCarte.getNom() + " de " + uneCarte.getCouleur())
#     
# for i in range(26):    
#     uneCarte = j_2.getCarteAt(i)
#     print("j2 : " + uneCarte.getNom() + " de " + uneCarte.getCouleur())



while j_1 != estVide() or j_2 != estVide():
    cartej_1 = j_1.tirerUneCarte()
    temp.ajouterCarte(cartej_1)
    cartej_2 = j_2.tirerUneCarte()
    temp.ajouterCarte(cartej_2)
# print(temp)
    
    
    
    

# Algorithme de la bataille
# tant que le jeu 1 n’est pas vide ou le jeu 2 n’est pas vide faire
# 	Prendre la carte du dessus du jeu 1 et la retourner.  
# 	Mettre cette carte sur le dessus de la pile de bataille 1
# 	Prendre la carte du dessus du jeu 2 et la retourner
# 	Mettre cette carte sur le dessus de la pile de bataille 2
# 	tant que les 2 cartes du dessus des piles de bataille sont  égales faire
# 		Prendre la carte du dessus du jeu 1
# 		Mettre cette carte face cachée sur le dessus de la pile de bataille 1
# 		Prendre la carte du dessus du jeu 1 et la retourner face visible
# 		Mettre cette carte sur le dessus de la pile de bataille 1
# 		Prendre la carte du dessus du jeu 2
# 		Mettre cette carte face cachée sur le dessus de la pile de bataille 2
# 		Prendre la carte du dessus du jeu 2 et la retourner face visible
# 		Mettre cette carte sur le dessus de la pile de bataille 2
# 	fin tant que
# 	Joueur gagnant ce tour : celui qui a la plus forte carte en sommet de pile de bataille
# 	tant que la pile de bataille 1 n’est pas vide faire
# 		Prendre la carte sur le dessus de la pile de bataille 1
# 		La glisser face cachée sous le paquet du gagnant
# 	fin tant que
# 	tant que la pile de bataille 2 n’est pas vide faire
# 		Prendre la carte sur le dessus de la pile de bataille 2
# 		La glisser sous le paquet du gagnant
# 	fin tant que
# fin tant que
# Le gagnant est celui qui a toutes les cartes dans son jeu





    
########
# distribuer
# 
# pour les cartes allant de 1 à 26 :
#     tirer une carte de paquet et la mettre dans j1
#     
# pour les cartes allant de 1 à 26 :
#     tirer une carte de paquet et la mettre dans j2
#####




   
    


