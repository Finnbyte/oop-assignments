class Asiakas:
    def __init__(self, nimi, ika):
        self.__nimi = nimi
        self.__ika = ika
        
    @property
    def nimi(self):
        return self.__nimi
    
    @property
    def ika(self):
        return self.__ika

    @nimi.setter
    def nimi(self, nimi):
        if nimi != "":
            self.__nimi = nimi
        else: raise ValueError("Anna epätyhjä nimi!")
        
    @ika.setter
    def ika(self, ika):
        if ika != "":
            self.__ika = ika
        else: raise ValueError("Anna epätyhjä ikä!")
        
class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        self.__edut = []
        super().__init__(tuotenimi)
