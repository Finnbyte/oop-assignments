class Asiakas:
    def __init__(self, nimi, ika):
        self.__nimi = nimi
        self.__ika = ika

class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

class ParempiPalvelu:
    pass


