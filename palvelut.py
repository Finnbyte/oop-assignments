import random

class Asiakas:
    """
    Luokka, joka kuvastaa "Asiakasta".
    Ottaa konstruktoriin argumenteiksi nimen ja iän.
    Luo itse satunnaisen arvon asiakkaan identifoivaksi numeroksi.
    """
    def __init__(self, nimi, ika):
        self.__nimi = nimi
        self.__ika = ika
        self.__asiakasnro = self.__luo_asiakasnro()
        
    @property
    def nimi(self):
        """
        Palauttaa Asiakkaan nimen.
        """
        return self.__nimi
    
    @property
    def ika(self):
        """
        Palauttaa Asiakkaan iän
        """
        return self.__ika

    def set_nimi(self, nimi):
        """ Asettaa nimi-muuttujan käyttäjän antamaan nimeen
        Mikäli nimi tyhjä, nostaa ValueError.
        """
        if nimi != "":
            self.__nimi = nimi
        else: raise ValueError("Anna epätyhjä nimi asiakkaalle!")
        
    @ika.setter
    def set_ika(self, ika):
        """ Asettaa ikä-muuttujan käyttäjän antamaan nimeen
        Mikäli ikä tyhjä, nostaa ValueError.
        """
        if ika != "":
            self.__ika = ika
        else: raise ValueError("Anna epätyhjä ikä!")

    @property
    def asiakasnro(self):
        """
        Palauttaa formatoidun version sisäisestä asiakasnumero-arvosta.
        """
        return f"{'-'.join(str(index) for index in self.__asiakasnro)}"

    def __luo_asiakasnro(self):
        """
        Palauttaa sisäisen ja satunnaisen arvon, joka esittää asiakasnumeroa.
        """
        return [
            random.randint(10, 99),
            random.randint(100, 999),
            random.randint(100, 999)
        ]

class Palvelu:
    """
    Luokka Palvelu määrittää "palvelun", jolla on nimi ja lista Asiakkaita.
    """
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def lisaa_asiakas(self, asiakas):
        """
        Lisää uuden Asiakas elementin asiakkaat-listaan.
        """
        if asiakas:
            self.__asiakkaat.append(asiakas)
        else: raise ValueError(f"Anna epätyhjä \"asiakas\"!")

    def poista_asiakas(self, asiakas):
        """
        Poistaa asiakkaat-listasta Asiakkaan.
        Jos asiakasta ei ole, ohittaa virheen
        """
        try:
            self.__asiakkaat.remove(asiakas)
        except ValueError:
            pass

    def _luo_asiakasrivi(self, asiakas):
        """ Suojattu metodi, joka formatoi asiakasrivin argumenttina annetun Asiakkaan perusteella.
        """
        return f"{asiakas.nimi} ({asiakas.asiakasnro}) on {asiakas.ika}-vuotias"
    
    def tulosta_asiakkaat(self):
        """
        Iteroi jokaisen asiakkaan yli ja tulostaa heidän tietonsa formatoituna käyttäen _luo_asiakasrivi-metodia.
        """
        for asiakas in self.__asiakkaat:
            print(self._luo_asiakasrivi(asiakas))
            
class ParempiPalvelu(Palvelu):
    """
    Luokka ParempiPalvelu periytyy Palvelusta, ja "etujen" luonnin, muokkauksen ja näytön.
    """
    def __init__(self, tuotenimi):
        self.__edut = []
        super().__init__(tuotenimi)

    def lisaa_etu(self, etu):
        """
        Lisää edun edut-listaan
        """
        if etu:
            self.__edut.append(etu)
        else: raise ValueError(f"Anna epätyhjä \"etu\"!")

        def poista_etu(self, etu):
        """
        Poistaa edut-listasta edun.
        Jos etua ei ole, ohittaa virheen.
        """
        try:
            self.__edut.remove(etu)
        except ValueError:
            pass
        
    def tulosta_edut(self):
        """
        Tulostaa edut-listan kaikki edut
        """
        print(f"Tuotteen {self.tuotenimi} edut ovat:")
        for etu in self.__edut:
            print(etu)
        
