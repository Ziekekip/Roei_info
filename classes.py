from collections import Counter


class Roeier:
    def __init__(self, naam, vereniging):
        """Creates a person with its attributes."""
        self.naam = naam
        self.vereniging = vereniging
    
    def __eq__(self, other):
        return self.naam == other.naam and self.vereniging == other.vereniging
    
    def __hash__(self):
        return hash(('naam', self.naam, 'vereniging', self.vereniging))
    
class Race:
    def __init__(self, veld, race, starttijd, ploeg1=None, ploeg2=None, ploeg3=None, ploeg4=None, ploeg5=None,
                 ploeg6=None, ):
        """Creates a Race with its attributes."""
        self.veld = veld
        self.race = race
        self.starttijd = starttijd
        self.ploeg1 = ploeg1
        self.ploeg2 = ploeg2
        self.ploeg3 = ploeg3
        self.ploeg4 = ploeg4
        self.ploeg5 = ploeg5
        self.ploeg6 = ploeg6


class TimeTrial:
    def __init__(self, veld, ploegen, race="time-trial", racetijd=None):
        self.veld = veld
        self.ploegen = ploegen
        self.race = race
        self.racetijd = racetijd



class Ploeg:
    def __init__(self, veld, ploegnaam, roeiers, boottype, stuur=None, verenigingen=None, rugnummer=None, blad=None):
        """Maakt een ploeg met de bijbehorende attributen"""
        self.veld = veld
        self.ploegnaam = ploegnaam
        if verenigingen is None or verenigingen == "":
            self.verenigingen = []
            for i in range(1, len(roeiers)):
                self.verenigingen.append(roeiers[len(roeiers) - i].vereniging)
            if stuur is not None and stuur.naam != "":
                self.verenigingen.append(stuur.vereniging)
            self.verenigingen = [item for items, c in Counter(self.verenigingen).most_common() for item in [items] * c]
            self.verenigingen = list(dict.fromkeys(self.verenigingen))
        else:
            self.verenigingen = verenigingen

        self.roeiers = roeiers
        self.boottype = boottype
        self.stuur = stuur
        self.rugnummer = rugnummer
        if blad is None or blad == "":
            self.blad = self.verenigingen[0]
        else:
            self.blad = blad

    def __eq__(self, other):
        return self.veld == other.veld and self.ploegnaam == other.ploegnaam and self.roeiers == other.roeiers

    def __hash__(self):
        return hash(('veld', self.veld, 'ploegnaam', self.ploegnaam, "roeiers", self.roeiers))


    def info(self):
        print("Ploegnaam: " + self.ploegnaam)
        if len(self.verenigingen) == 1:
            print("Vereniging: " + self.verenigingen[0])
        else:
            print("Verenigingen: " + self.verenigingen[0], end="")
            for i in range(1, len(self.verenigingen)):
                print("-" + self.verenigingen[i], end="")
            print("")
        print("Veld: " + self.veld)
        print("Roeiers:")
        if "8" in self.boottype:
            for i in range(1, 9):
                print(str(i) + ": " + self.roeiers[i].naam)
        elif "4" in self.boottype:
            for i in range(1, 5):
                print(str(i) + ": " + self.roeiers[i].naam)
        elif "2" in self.boottype:
            for i in range(1, 3):
                print(str(i) + ": " + self.roeiers[i].naam)
        elif "1" in self.boottype:
            print("1: " + self.roeiers[1].naam)
        if self.stuur is not None:
            print("Stuur: " + self.stuur.naam)
        print("Boottype: " + self.boottype)
        if self.rugnummer is not None:
            print("Rugnummer: " + str(self.rugnummer))
        print("Blad: " + self.blad)