from main import *
import requests
from bs4 import BeautifulSoup
from main import *
import pickle
import re
from classes import *

def tt_veld_race_getter(string):
    string_list = string.split(" ")
    
    if string_list[-1] == "heat":
        race = string_list[-1]
        veld = ""
        for i in range(len(string_list) - 1):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld) - 1]
    elif string_list[-1] == "time-trial":
        race = "time-trial"
        veld = ""
        for i in range(len(string_list) - 1):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld) - 1]
    elif string_list[-1] == "Lanes":
        race = "Race For Lanes"
        veld = ""
        for i in range(len(string_list) - 3):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld) - 1]
    elif re.match(".-finale", string_list[-1]):
        race = string_list[-1]
        veld = ""
        for i in range(len(string_list) - 1):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld) - 1]
    elif string_list[-2] == "voorwedstrijd":
        race = string_list[-2] + " " + string_list[-1]
        veld = ""
        for i in range(len(string_list) - 2):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld) - 1]
    elif string_list[-2] == "herkansing":
        race = string_list[-2] + " " + string_list[-1]
        veld = ""
        for i in range(len(string_list) - 2):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld) - 1]
    elif string_list[-2] == "halve-finale":
        race = string_list[-2] + " " + string_list[-1]
        veld = ""
        for i in range(len(string_list) - 2):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld) - 1]
    elif string_list[-2] == "kwart-finale":
        race = string_list[-2] + " " + string_list[-1]
        veld = ""
        for i in range(len(string_list) - 2):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld) - 1]
    else:
        veld = string
        race = string


    return veld, race


def tt_get_races(wedstrijdpagina):
    page = requests.get(wedstrijdpagina)
    print("request wedstrijd: " + wedstrijdpagina)
    race_tijden = []
    race_naam = []
    race_link = []
    race_nummer = []

    soup = BeautifulSoup(page.content, 'html.parser')
    races = list(soup.find_all('tr', {'class': ['odd', 'even']}))
    for i in range(len(races)):

        info = races[i].find_all('td')
        if info[0].get_text() != "" and "href" in str(races[i].find_all('td')[2]):
            race_tijden.append(info[0].get_text())
            race_naam.append(info[2].get_text())
            race_nummer.append(info[1].get_text())
            race_link.append(races[i].find_all('td')[2].a["href"])

    races = [race_nummer, race_tijden, race_naam, race_link, []]
    return races


def tt_get_ploegen(wedstrijdpagina, racelink):
    ploeg_baan = []
    ploeg_rugnummer = []
    ploeg_vereniging = []
    ploeg_naam = []
    ploeg_link = []

    page = requests.get(wedstrijdpagina[:len(wedstrijdpagina) - wedstrijdpagina[::-1].find("/")] + racelink)
    print("request race: " + racelink)

    soup = BeautifulSoup(page.content, 'html.parser')

    ploegen = list(soup.find_all('tr', {'class': ['odd', 'even']}))
    for i in range(len(ploegen)):

        info = ploegen[i].find_all('td')
        if info[0].get_text() != "" and "href" in str(ploegen[i].find_all('td')[2]):
            ploeg_baan.append(int(info[0].get_text()[1:][:-1]))
            ploeg_naam.append(info[2].get_text())
            ploeg_vereniging.append(info[1].get_text())
            ploeg_link.append(ploegen[i].find_all('td')[2].a["href"][3:])
            if len(info) <= 3:
                ploeg_rugnummer.append(None)
            else:
                if info[3].get_text()[1:][:-1].isnumeric():
                    ploeg_rugnummer.append(int(info[3].get_text()[1:][:-1]))
                else:
                    ploeg_rugnummer.append(None)

    ploegen = [ploeg_baan, ploeg_rugnummer, ploeg_vereniging, ploeg_naam, ploeg_link]
    return ploegen


def tt_get_ploegen_timetrial(wedstrijdpagina, racelink):
    
    ploeg_rugnummer = []
    ploeg_vereniging = []
    ploeg_naam = []
    ploeg_link = []

    page = requests.get(wedstrijdpagina[:len(wedstrijdpagina) - wedstrijdpagina[::-1].find("/")] + racelink)
    print("request race: " + racelink)

    soup = BeautifulSoup(page.content, 'html.parser')

    ploegen = list(soup.find_all('tr', {'class': ['odd', 'even']}))
    for i in range(len(ploegen)):
        
        info = ploegen[i].find_all('td')
        if len(info[0].get_text()) == 3:
        
            
            
            
            ploeg_naam.append(info[1].get_text())
            ploeg_vereniging.append(info[0].get_text())
            ploeg_link.append(ploegen[i].find_all('td')[1].a["href"][3:])
            ploeg_rugnummer.append(info[2].get_text()[1:][:-1])
        
        

    ploegen = [None, ploeg_rugnummer, ploeg_vereniging, ploeg_naam, ploeg_link]
    return ploegen


def tt_get_roeiers(wedstrijdpagina, ploeglink):
    test = len(wedstrijdpagina[::-1]) - len(wedstrijdpagina[::-1].split("/", 2)[-1]) - len("/")
    page = requests.get(wedstrijdpagina[:len(wedstrijdpagina) - test] + ploeglink)
    print("request ploeg: " + ploeglink)
    soup = BeautifulSoup(page.content, 'html.parser')

    roeiers = []
    stuur = None
    roeiers_info = list(soup.find_all('tr', {'class': ['odd', 'even']}))
    for i in range(len(roeiers_info)):

        info = roeiers_info[i].find_all('td')

        # print(info[1].get_text())
        # print(info[0].get_text())
        if "cox" in info[0].get_text():
            if info[1].get_text() != "":
                stuur = info[1].get_text()
        else:
            roeiers.append(info[1].get_text())

    return roeiers, stuur

def tt_maakploeg(wedstrijdpagina, rugnummer, vereniging, ploegnaam, ploeglink, racenaam):
    roeiers_raw, stuur_raw = tt_get_roeiers(wedstrijdpagina, ploeglink)
    roeiers = []
    for i in range(len(roeiers_raw)):
        roeiers.append(Roeier(roeiers_raw[i], vereniging))
    if stuur_raw is not None:
        stuur = Roeier(stuur_raw, vereniging)
    else:
        stuur = None






    if "-finale" in racenaam:
        veld = racenaam[:len(racenaam) - 9]
    elif "voorwedstrijd " in racenaam:
        veld = racenaam[:len(racenaam) - 15]
    elif " heat" in racenaam:
        veld = racenaam[:len(racenaam) - 5]
    else:
        veld = racenaam


    boottype = ""
    if "NSRF" in veld:
        boottype = "C4+"
    elif "C4+" in veld:
        boottype = "C4+"
    elif "C4*" in veld:
        boottype = "C4*"
    elif "C2+" in veld:
        boottype = "C2+"
    elif "C2*" in veld:
        boottype = "C2*"
    elif "1x" in veld:
        boottype = "1x"
    elif "2x" in veld:
        boottype = "2x"
    elif "2-" in veld:
        boottype = "2-"
    elif "2+" in veld:
        boottype = "2+"
    elif "4x" in veld:
        boottype = "4x"
    elif "4-" in veld:
        boottype = "4-"
    elif "4*" in veld:
        boottype = "4*"
    elif "4+" in veld:
        boottype = "4+"
    elif "8+" in veld:
        boottype = "8+"




    ploeg = Ploeg(veld, ploegnaam, roeiers, boottype, stuur, [vereniging], rugnummer)
    return ploeg


def tt_maaktimetrial(wedstrijdpagina, racelink, racenaam, racetijd):
    ploegen_raw = tt_get_ploegen_timetrial(wedstrijdpagina, racelink)
    ploegen = []
    
    for i in range(len(ploegen_raw[1])):
        ploeg = tt_maakploeg(wedstrijdpagina, ploegen_raw[1][i], ploegen_raw[2][i], ploegen_raw[3][i], ploegen_raw[4][i], racenaam)
        ploegen.append(ploeg)
    
    veldnaam = ploegen[0].veld
    
    
    
    veld, race = tt_veld_race_getter(racenaam)
    timetrial = TimeTrial(veld, ploegen, race, racetijd)
    print("veldnaam: " + timetrial.veld)
    return timetrial
    
    
def tt_maakrace(wedstrijdpagina, racelink, racenaam, racetijd):




    ploegen_raw = tt_get_ploegen(wedstrijdpagina, racelink)
    ploegen = []
    for i in range(len(ploegen_raw[0])):
        ploeg = tt_maakploeg(wedstrijdpagina, ploegen_raw[1][i], ploegen_raw[2][i], ploegen_raw[3][i], ploegen_raw[4][i], racenaam)
        ploegen.append(ploeg)


    baan1 = None
    baan2 = None
    baan3 = None
    baan4 = None
    baan5 = None
    baan6 = None

    for i in range(len(ploegen)):
        if ploegen_raw[0][i] == 1:
            baan1 = ploegen[i]
        if ploegen_raw[0][i] == 2:
            baan2 = ploegen[i]
        if ploegen_raw[0][i] == 3:
            baan3 = ploegen[i]
        if ploegen_raw[0][i] == 4:
            baan4 = ploegen[i]
        if ploegen_raw[0][i] == 5:
            baan5 = ploegen[i]
        if ploegen_raw[0][i] == 6:
            baan6 = ploegen[i]
        if ploegen_raw[0][i] == 7 and baan1 is not None:
            baan1 = baan2
            baan2 = baan3
            baan3 = baan4
            baan4 = baan5
            baan5 = baan6
            baan6 = ploegen[i]



    veld, race = tt_veld_race_getter(racenaam)



    race = Race(veld, race, racetijd, baan1, baan2, baan3, baan4, baan5, baan6)

    return race


def tt_nth_occurence(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)



def tt_maakwedstrijd(wedstrijdpagina, jaar=None):
    if jaar is None or jaar == "":
        jaar = wedstrijdpagina[int(tt_nth_occurence(wedstrijdpagina, "/", 3)) + 1: int(tt_nth_occurence(wedstrijdpagina, "/", 4))]
    
     


    races_raw = tt_get_races(wedstrijdpagina)
    races = []

    for i in range(len(races_raw[0])):
        if "time-trial" in races_raw[2][i]:
            timetrial = tt_maaktimetrial(wedstrijdpagina, races_raw[3][i], races_raw[2][i], races_raw[1][i])
            races.append(timetrial)
        else:
            race = tt_maakrace(wedstrijdpagina, races_raw[3][i], races_raw[2][i], races_raw[1][i])
            races.append(race)
    totaal = [jaar, races]
    return totaal



def tt_pickle_wedstrijd(wedstrijd, naam):
    pickle_out = open("pickle/" + naam + ".pickle", "wb")
    pickle.dump(wedstrijd, pickle_out)
    pickle_out.close()
    print(naam + " is gemaakt")


def tt_unpickle_wedstrijd(naam):
    pickle_in = open("pickle/" + naam + ".pickle", "rb")
    return pickle.load(pickle_in)



