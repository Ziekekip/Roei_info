import re
import urllib.parse
from hs_scraper import *

switcher = {
    "AEG": "Aegir",
    "AGO": "Agon",
    "AMP": "Amphitrite",
    "ARG": "Argo",
    "ASO": "Asopos",
    "BOR": "Boreas",
    "EUR": "Euros",
    "LAG": "Laga",
    "NJO": "Njord",
    "OKE": "Okeanos",
    "ORC": "Orca",
    "PEL": "Pelargos",
    "PHO": "Phocas",
    "PRO": "Proteus",
    "SAU": "Saurus",
    "SKA": "Skadi",
    "SKO": "Skoll",
    "THE": "Theta",
    "TRI": "Triton",
    "VID": "Vidar"
}

# inv_map = {v: k for k, v in switcher.items()}
# print({v: k for k, v in switcher.items()})

vw1 = "DOnerv C4+ voorwedstrijd 1"
vw2 = "DOnerv C4+ voorwedstrijd 12"

hk1 ="DOnerv C4+ herkansing 2"
hk2 = "DOnerv C4+ herkansing 12"

af = "DOnerv C4+ A-finale"
bf = "DOnerv C4+ B-finale"

ht = "DOnerv C4+ heat"

RL = "DOnerv C4+ Race for Lanes"

hf = "DOnerv C4+ halve-finale 1"
kf = "DOnerv C4+ kwart-finale 1"


def veld_race_getter(string):

    string_list = string.split(" ")
    print(string_list)
    if string_list[-1] == "heat":
        race = string_list[-1]
        veld = ""
        for i in range(len(string_list)-1):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld)-1]
    elif string_list[-1] == "Lanes":
        race = "Race For Lanes"
        veld = ""
        for i in range(len(string_list)-3):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld)-1]
    elif re.match(".-finale", string_list[-1]):
        race = string_list[-1]
        veld = ""
        for i in range(len(string_list) - 1):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld) - 1]
    elif string_list[-2] == "voorwedstrijd":
        race = string_list[-2] + " " + string_list[-1]
        veld = ""
        for i in range(len(string_list)-2):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld)-1]
    elif string_list[-2] == "herkansing":
        race = string_list[-2] + " " + string_list[-1]
        veld = ""
        for i in range(len(string_list)-2):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld)-1]
    elif string_list[-2] == "halve-finale":
        race = string_list[-2] + " " + string_list[-1]
        veld = ""
        for i in range(len(string_list)-2):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld)-1]
    elif string_list[-2] == "kwart-finale":
        race = string_list[-2] + " " + string_list[-1]
        veld = ""
        for i in range(len(string_list)-2):
            veld = veld + string_list[i] + " "
        veld = veld[:len(veld)-1]


    return veld, race


#print(urllib.parse.quote("DEj 8+"))

wedstrijdpagina = "https://hoesnelwasik.nl/herfst/2020/loting#"


jaar = wedstrijdpagina[int(hs_nth_occurence(wedstrijdpagina, "/", 3)) + 1: int(hs_nth_occurence(wedstrijdpagina, "/", 4))]

print(jaar)