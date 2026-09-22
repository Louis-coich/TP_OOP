from multipledispatch import dispatch


class Habitant:

    def __init__(self, nom, age, adresse, animaux=None):
        self.__nom = nom
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}
        self.age = age  # passe par le setter pour valider la valeur

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_adresse(self):
        return self.__adresse

    def set_adresse(self, adresse):
        self.__adresse = adresse

    def get_animaux(self):
        return self.__animaux

    def set_animaux(self, animaux):
        self.__animaux = animaux

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, valeur):
        if valeur < 0 or valeur > 130:
            raise ValueError("L'age doit etre compris entre 0 et 130.")
        self.__age = valeur

    def affichage_adresse(self):
        print(f"{self.__nom} habite a {self.__adresse}")

    def compte_animal(self, animal):
        return self.__animaux.get(animal, 0)


@dispatch(object, str)
def set_info(habitant, nom):
    habitant.set_nom(nom)


@dispatch(object, str, int)
def set_info(habitant, nom, age):  # pylint : disable = function - redefined
    habitant.set_nom(nom)
    habitant.set_age(age)





