import random

class Asiakas:
    def __init__(self, nimi, ika):
        self.__nimi = nimi
        self.__ika = ika
        self.__asiakasnro = self.__luo_asiakasnro()
        
    @property
    def nimi(self):
        return self.__nimi
    
    @property
    def ika(self):
        return self.__ika

    def set_nimi(self, nimi):
        if nimi != "":
            self.__nimi = nimi
        else: raise ValueError("Anna epätyhjä nimi asiakkaalle!")
        
    @ika.setter
    def set_ika(self, ika):
        if ika != "":
            self.__ika = ika
        else: raise ValueError("Anna epätyhjä ikä!")

    @property
    def asiakasnro(self):
        return f"{'-'.join(str(index) for index in self.__asiakasnro)}"

    def __luo_asiakasnro(self):
        return [
            random.randint(10, 99),
            random.randint(100, 999),
            random.randint(100, 999)
        ]

class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []
        
    def lisaa_asiakas(self, asiakas):
        if asiakas:
            self.__asiakkaat.append(asiakas)
        else: raise ValueError(f"Anna epätyhjä \"asiakas\"!")
        
    def poista_asiakas(self, asiakas):
        try:
            self.__asiakkaat.remove(asiakas)
        except ValueError:
            pass
        
    def _luo_asiakasrivi(self, asiakas):
        return f"{asiakas.nimi} ({asiakas.asiakasnro}) on {asiakas.ika}-vuotias"
    
    def tulosta_asiakkaat(self):
        for asiakas in self.__asiakkaat:
            print(self._luo_asiakasrivi(asiakas))
            
class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        self.__edut = []
        super().__init__(tuotenimi)
        
    def lisaa_etu(self, etu):
        if etu:
            self.__edut.append(etu)
        else: raise ValueError(f"Anna epätyhjä \"etu\"!")
        
    def poista_etu(self, etu):
        try:
            self.__edut.remove(etu)
        except ValueError:
            pass
        
    def tulosta_edut(self):
        print(f"Tuotteen {self.tuotenimi} edut ovat:")
        for etu in self.__edut:
            print(etu)
        
