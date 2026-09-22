from multipledispatch import dispatch
from habitant import Habitant


class Village:

    def __init__(self, nom):
        self.__nom = nom
        self.__habitants = []

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        self.__habitants.append(Habitant(nom, age, adresse, animaux))

    def ajouter_habitant_agregation(self, habitant):
        self.__habitants.append(habitant)

    def afficher_habitants(self):
        for habitant in self.__habitants:
            habitant.affichage_adresse()

    def get_nom(self):
        return self.__nom

    def get_habitants(self):
        return self.__habitants




