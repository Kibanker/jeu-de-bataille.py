import random
import tkinter as tk

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
        elif self.Valeur == 14:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle)"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur-1]   # ATTENTION ! problème d'indice !
    
    def image(self) :
        """
        méthode permettant l'affichage d'une carte"
        """
        fichier = "modele_cartes/"+ str(self.Valeur) + self.couleur + ".GIF"
        fenetre = tk.Tk()
        #fenetre.geometry ("935 x 692 ")
        image_carte = tk.PhotoImage(file = fichier)
        label = tk.Label (fenetre, image = image_carte)
        label.pack()
        fenetre.mainloop()

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
        
    """
        Permet de tirer la carte se trouvant aux sommet du paquet
        de chaque joueur
    """
    def tirerUneCarte(self):
        carte = self.contenu[-1]
        self.contenu.pop()
        return carte

    def ajouterCarte(self, carte):
        self.contenu.append(carte)
        return carte
        
    def estVide(self):
        return (self.contenu == [])                       

    def taille(self):
        return len(self.contenu)
    
class Bataille:
    
#     def __init__(self):
    
    def affrontement(self, carte1, carte2):
        if (self.Valeur(carte1) > self.Valeur(carte2)):
            return "Joueur 1 gagne"
        elif (self.Valeur(carte1) == self.Valeur(carte2)):
            return "Egalité"
        else:
            return "Joueur 2 gagne"
        
        
        
    

unPaquet = PaquetDeCarte()
unPaquet.remplir()
unPaquet.melanger()
j_1 = PaquetDeCarte()
j_2 = PaquetDeCarte()
temp = PaquetDeCarte()
bat = Bataille()
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
# for i in range(26):    
#     uneCarte = j_2.getCarteAt(i)
#     print("j2 : " + uneCarte.getNom() + " de " + uneCarte.getCouleur())



while j_1.estVide() == False or j_2.estVide() == False:
    cartej_1 = j_1.tirerUneCarte()
    temp.ajouterCarte(cartej_1)    
    cartej_2 = j_2.tirerUneCarte()
    temp.ajouterCarte(cartej_2)
print(cartej_1.getNom() + " de " + cartej_1.getCouleur())
print(cartej_2.getNom() + " de " + cartej_2.getCouleur())


    
    
    
    
    
    
    
    
    
#     while cartej_1.getNom() == cartej_2.getNom():
#         cartej_1 = j_1.tirerUneCarte()
#         temp.ajouterCarte(cartej_1)
#         cartej_2 = j_2.tirerUneCarte()
#         temp.ajouterCarte(cartej_2)
#     if (cartej_1.getNom() > cartej_2.getNom()):
#         while j_1.estVide() != True:
#             j_1.ajouterCarte(cartej_1)
#             j_1.ajouterCarte(cartej_2)
#     elif (cartej_1.getNom() < cartej_2.getNom()):
#         while j_2.estVide() != True:
#             j_2.ajouterCarte(cartej_1)
#             j_2.ajouterCarte(cartej_2)
# if (j_1.taille() == 52):
#     print("Le joueur 1 a gagné")
# else:
#     print("Le joueur 2 a gagné")
        
            
        
        

    
    
    
    

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
