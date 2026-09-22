from multipledispatch import dispatch
from habitant import Habitant


class Village:
    """Un village qui regroupe des habitants."""

    def __init__(self, nom):
        """Initialise le village avec un nom et une liste d'habitants vide."""
        self.__nom = nom
        self.__habitants = []

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        """Cree un nouvel habitant et l'ajoute (le village en est proprietaire)."""
        self.__habitants.append(Habitant(nom, age, adresse, animaux))

    def ajouter_habitant_agregation(self, habitant):
        """Ajoute un habitant qui existe deja (partage possible entre villages)."""
        self.__habitants.append(habitant)

    def afficher_habitants(self):
        """Affiche chaque habitant du village."""
        for habitant in self.__habitants:
            habitant.affichage_adresse()

    def get_nom(self):
        """Renvoie le nom du village."""
        return self.__nom

    def get_habitants(self):
        """Renvoie la liste des habitants."""
        return self.__habitants




