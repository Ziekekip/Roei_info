import time
import urllib.request
import operator
from classes import *
import main
import requests
from bs4 import BeautifulSoup
import json
import pickle


def hs_nth_occurence(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)


def hs_maak_wedstrijd(wedstrijdpagina, jaar=None):
    if jaar is None or jaar == "":
        jaar = wedstrijdpagina[int(hs_nth_occurence(wedstrijdpagina, "/", 3)) + 1: int(hs_nth_occurence(wedstrijdpagina, "/", 4))]
    
    
    
    
    velden_raw = hs_get_velden(wedstrijdpagina)
    velden = []
    print(velden_raw)
    for i in range(len(velden_raw)):
        velden.append(hs_maak_veld(wedstrijdpagina, velden_raw[i]))
    
    wedstrijd = [jaar, velden]
    return wedstrijd


def hs_get_velden(wedstrijdpagina):
    velden_pagina = "https://hoesnelwasik.nl/api/wd" + wedstrijdpagina[hs_nth_occurence(wedstrijdpagina, "/", 2):hs_nth_occurence(wedstrijdpagina, "/", 4)] + "/velden/"
    
    page = requests.get(velden_pagina)
    print("Requesting velden: " + velden_pagina)
    soup = BeautifulSoup(page.content, 'lxml')
    
    html = list(soup.children)[0]
    
    body = list(html.children)[0]
    
    p = list(body.children)[0]
    
    data_raw = p.get_text()
    
    data_json = json.loads(data_raw)
    
    velden = []
    blok = []
    plek_in_blok = []
    for field in data_json['fields']:
        if "fieldnameshort" in field and "blocknumber" in field and "startorder" in field:
            if field["fieldnameshort"] is not None and field["blocknumber"] is not None and field["startorder"] is not None:
                velden.append([field["fieldnameshort"], int(field["blocknumber"]), int(field["startorder"])])
        
        
    #velden = velden[1::2]
    for i in range(len(velden)):
        print(velden[i])
    velden_sorted = sorted(velden, key=lambda x: (x[1], x[2]))
    velden_final = []
    
    
    for i in range(len(velden_sorted)):
        print(velden_sorted[i])
    
    
    for veld in velden_sorted:
        
        velden_final.append(veld[0])
    
    
    for i in range(len(velden_final)):
        print(velden_final[i][0])
    
    velden_final_2 = []
    for item in velden_final:
        if item not in velden_final_2:
            velden_final_2.append(item)
    
    
    return velden_final_2


def hs_maak_veld(wedstrijdpagina, veldnaam):
    veld_pagina = "https://hoesnelwasik.nl/api/wd" + wedstrijdpagina[hs_nth_occurence(wedstrijdpagina, "/", 2):hs_nth_occurence(wedstrijdpagina, "/", 4)] + "/" + urllib.parse.quote(veldnaam) + "/loting"
    

    page = requests.get(veld_pagina)
    print("Requesting veld " + veldnaam + ": " + veld_pagina)
    
    soup = BeautifulSoup(page.content, 'lxml')

    html = list(soup.children)[0]

    body = list(html.children)[0]

    p = list(body.children)[0]

    data_raw = p.get_text()

    data_json = json.loads(data_raw)

    boottype = ""
    if "NSRF" in veldnaam:
        boottype = "C4+"
    elif "C4+" in veldnaam:
        boottype = "C4+"
    elif "C4*" in veldnaam:
        boottype = "C4*"
    elif "C2+" in veldnaam:
        boottype = "C2+"
    elif "C2*" in veldnaam:
        boottype = "C2*"
    elif "1x" in veldnaam:
        boottype = "1x"
    elif "2x" in veldnaam:
        boottype = "2x"
    elif "2-" in veldnaam:
        boottype = "2-"
    elif "2+" in veldnaam:
        boottype = "2+"
    elif "4x" in veldnaam:
        boottype = "4x"
    elif "4-" in veldnaam:
        boottype = "4-"
    elif "4*" in veldnaam:
        boottype = "4*"
    elif "4+" in veldnaam:
        boottype = "4+"
    elif "8+" in veldnaam:
        boottype = "8+"
    
    
    ploegen = []
    
    for team in data_json['teams']:
        vereniging = team["clubnameshort"]
        roeiers_raw = []
        if "rower1" in team.keys():
            roeiers_raw.append(team["rower1"])
        if "rower2" in team.keys():
            roeiers_raw.append(team["rower2"])
        if "rower3" in team.keys():
            roeiers_raw.append(team["rower3"])
        if "rower4" in team.keys():
            roeiers_raw.append(team["rower4"])
        if "rower5" in team.keys():
            roeiers_raw.append(team["rower5"])
        if "rower6" in team.keys():
            roeiers_raw.append(team["rower6"])
        if "rower7" in team.keys():
            roeiers_raw.append(team["rower7"])
        if "rower8" in team.keys():
            roeiers_raw.append(team["rower8"])
        
        
        roeiers = []
        for i in range(len(roeiers_raw)):
            roeiers.append(Roeier(roeiers_raw[i], vereniging))
        stuur = None
        if "steername" in team.keys():
            stuur = Roeier(team["steername"], vereniging)
        rugnummer = None
        if "backnumber" in team.keys():
            rugnummer = team["backnumber"]
        
        
        ploeg = Ploeg(veldnaam, team["teamname"], roeiers, boottype, stuur, [vereniging], rugnummer)
        ploegen.append(ploeg)
        
        
        
    ploegen_final = []
    for item in ploegen:
        if item not in ploegen_final:
            ploegen_final.append(item)
    
    
    timetrial = TimeTrial(veldnaam, ploegen_final)
        
    return timetrial
    
    
    
def hs_pickle_wedstrijd(wedstrijd, naam):
    pickle_out = open("pickle/" + naam + ".pickle", "wb")
    pickle.dump(wedstrijd, pickle_out)
    pickle_out.close()
    print(naam + " is gemaakt")

def hs_unpickle_wedstrijd(naam):
    pickle_in = open("pickle/" + naam + ".pickle", "rb")
    return pickle.load(pickle_in)
    
    
    
    
    
    

# print(json.dumps(data_json, indent=4, sort_keys=True))

# print(type(data_json))
#print(hs_maak_wedstrijd("https://hoesnelwasik.nl/herfst/0/loting#")[0].ploegen[15].roeiers[0].naam)



