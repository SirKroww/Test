from test import *

class Voiture(Vehicule):

    def __init__(self,marque,couleur):
        self.marque = "ferrari"
        #self.vitesse = 350.5
        self.couleur = couleur


    def __getattribute__(self,nom):
        print()
    
    def getMarque(self):
        return self.marque
    
    def setVitesse(self,a):
        if a<100:
            print("error")
        self.vitesse = a

    def klaxon(self):
        print("pouette")


c = Couleur(255,0,0)
v = Voiture("t",c)
