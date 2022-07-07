import msvcrt
import time
from collections import Counter
import pygame
import os
import pickle
import sys
from select import select
import signal
from classes import *


def afkorting_naar_naam(vereniging):
    """Krijgt als input een verenigingsafkorting, en retouneerd de gehele naam."""
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
        "SKO": "Skøll",
        "THE": "Theta",
        "TRI": "Triton",
        "VID": "Vidar",
        "NER": "Nereus",
        "GYA": "Gyas"

    }
    return switcher.get(vereniging, vereniging)


def naam_naar_afkorting(vereniging):
    """Krijgt als input een verenigingsnaam, en retouneerd de afkorting"""
    switcher = {
        'Aegir': 'AEG',
        'Agon': 'AGO',
        'Amphitrite': 'AMP',
        'Argo': 'ARG',
        'Asopos': 'ASO',
        'Boreas': 'BOR',
        'Euros': 'EUR',
        'Laga': 'LAG',
        'Njord': 'NJO',
        'Okeanos': 'OKE',
        'Orca': 'ORC',
        'Pelargos': 'PEL',
        'Phocas': 'PHO',
        'Proteus': 'PRO',
        'Saurus': 'SAU',
        'Skadi': 'SKA',
        'Skøll': 'SKO',
        'Skoll': 'SKO',
        'Theta': 'THE',
        'Triton': 'TRI',
        'Vidar': 'VID',
        'Nereus': 'NER',
        'Gyas': 'GYA'
    }
    return switcher.get(vereniging, vereniging)




def draw_background(baan, gameDisplay):
    """Doet de achtergrondaafbeelding op het scherm verschijnen in de behorende baan"""
    if baan in [1,4,7,10,13]:
        gameDisplay.blit(pygame.image.load('assets/achtergrond.png'), (0 + 640*(baan-1), 0))
        gameDisplay.blit(pygame.image.load('assets/ad_mask.png'), (0 + 640*(baan-1), 0))



def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


def draw_ploegheader(ploeg, baan, gameDisplay, jaar):
    """Doet algemene ploeginformatie op het scherm verschijnen in de behorende baan"""
    blit_alpha(gameDisplay, pygame.image.load('assets/Ploegheader2.png'), (0 + (baan - 1) * 640, 27), 255)

    blad = "bladen/" + jaar + "/" + ploeg.blad + ".png"
    if os.path.exists(blad) is False:
        blad = "bladen/" + ploeg.blad + ".png"
    if os.path.exists(blad) is False:
        blad = "bladen/blanco.png"

    blad = pygame.image.load(blad)
    blad = pygame.transform.scale(blad, (146, 53))

    gameDisplay.blit(blad, (448 + (baan - 1) * 640, 37))

    ploegnaamfont = pygame.font.SysFont("arial", 32)
    ploegnaamsurface = ploegnaamfont.render(ploeg.ploegnaam, 4, yellow)

    if ploegnaamsurface.get_width() >= 293:
        ploegnaamfont = pygame.font.SysFont("arial", 21)
        ploegnaamsurface = ploegnaamfont.render(ploeg.ploegnaam, 4, yellow)
        if ploegnaamsurface.get_width() >= 293:
            ploegnaamfont = pygame.font.SysFont("arial", 16)
            ploegnaamsurface = ploegnaamfont.render(ploeg.ploegnaam, 4, yellow)
            if ploegnaamsurface.get_width() >= 293:
                ploegnaamfont = pygame.font.SysFont("arial", 13)
                ploegnaamsurface = ploegnaamfont.render(ploeg.ploegnaam, 4, yellow)
                gameDisplay.blit(ploegnaamsurface, (37 + (baan - 1) * 640, 56))
            else:
                gameDisplay.blit(ploegnaamsurface, (37 + (baan - 1) * 640, 53))
        else:
            gameDisplay.blit(ploegnaamsurface, (37 + (baan - 1) * 640, 51))
    else:
        gameDisplay.blit(ploegnaamsurface, (37 + (baan - 1) * 640, 43))

    if len(ploeg.verenigingen) == 1:
        verenigingenstring = afkorting_naar_naam(ploeg.verenigingen[0])
        verenigingenfont = pygame.font.SysFont("arial", 16)
        verenigingensurface = verenigingenfont.render(verenigingenstring, 4, white)

        print(verenigingensurface.get_width())


        gameDisplay.blit(verenigingensurface, (389 - (verenigingensurface.get_width() / 2) + (baan - 1) * 640, 53))

    elif len(ploeg.verenigingen) == 2:
        verenigingenstring1 = afkorting_naar_naam(ploeg.verenigingen[0])
        verenigingenstring2 = afkorting_naar_naam(ploeg.verenigingen[1])
        verenigingenfont = pygame.font.SysFont("arial", 16)
        verenigingensurface1 = verenigingenfont.render(verenigingenstring1, 4, white)
        verenigingensurface2 = verenigingenfont.render(verenigingenstring2, 4, white)
        gameDisplay.blit(verenigingensurface1, (389 - (verenigingensurface1.get_width() / 2) + (baan - 1) * 640, 43))
        gameDisplay.blit(verenigingensurface2, (389 - (verenigingensurface2.get_width() / 2) + (baan - 1) * 640, 64))

    else:
        verenigingenstring1 = afkorting_naar_naam(ploeg.verenigingen[0])
        verenigingenstring2 = "combinatie"
        verenigingenfont = pygame.font.SysFont("arial", 16)
        verenigingensurface1 = verenigingenfont.render(verenigingenstring1, 4, white)
        verenigingensurface2 = verenigingenfont.render(verenigingenstring2, 4, white)
        gameDisplay.blit(verenigingensurface1, (389 - (verenigingensurface1.get_width() / 2) + (baan - 1) * 640, 43))
        gameDisplay.blit(verenigingensurface2, (389 - (verenigingensurface2.get_width() / 2) + (baan - 1) * 640, 64))


def draw_bootje(ploeg, baan, gameDisplay):
    """Displayed het boottype van een gegeven ploeg in de behorende baan"""
    if ploeg.boottype == "1x":
        bootje = pygame.image.load('boten/1x.png')
        bootje = pygame.transform.scale(bootje, (129, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "2x":
        bootje = pygame.image.load('boten/2x.png')
        bootje = pygame.transform.scale(bootje, (147, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "2+":
        bootje = pygame.image.load('boten/2+.png')
        bootje = pygame.transform.scale(bootje, (134, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "2-":
        bootje = pygame.image.load('boten/2-.png')
        bootje = pygame.transform.scale(bootje, (109, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "4-":
        bootje = pygame.image.load('boten/4-.png')
        bootje = pygame.transform.scale(bootje, (141, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "4+":
        bootje = pygame.image.load('boten/4+.png')
        bootje = pygame.transform.scale(bootje, (147, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "4x":
        bootje = pygame.image.load('boten/4x.png')
        bootje = pygame.transform.scale(bootje, (179, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "4*":
        bootje = pygame.image.load('boten/4x+.png')
        bootje = pygame.transform.scale(bootje, (186, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "8+":
        bootje = pygame.image.load('boten/8+.png')
        bootje = pygame.transform.scale(bootje, (171, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "C4+":
        bootje = pygame.image.load('boten/C4+.png')
        bootje = pygame.transform.scale(bootje, (147, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "C4*":
        bootje = pygame.image.load('boten/C4x+.png')
        bootje = pygame.transform.scale(bootje, (183, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "C2+":
        bootje = pygame.image.load('boten/C2+.png')
        bootje = pygame.transform.scale(bootje, (124, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))
    elif ploeg.boottype == "C2*":
        bootje = pygame.image.load('boten/C2x+.png')
        bootje = pygame.transform.scale(bootje, (155, 53))
        gameDisplay.blit(bootje, (133 + (baan - 1) * 640, 128))


def draw_ploegheaderinfo(ploeg, baan, race, gameDisplay):
    """Doet aanvullende ploeginformatie op het scherm verschijnen in de behorende baan"""
    gameDisplay.blit(pygame.image.load('assets/Ploegheaderonder.png'), (0 + (baan - 1) * 640, 117))

    boottypenaamfont = pygame.font.SysFont("arial", 32)
    boottypenaamsurface = boottypenaamfont.render(ploeg.boottype, 4, yellow)
    gameDisplay.blit(boottypenaamsurface, (37 + (baan - 1) * 640, 133))

    veldnaamfont = pygame.font.SysFont("arial", 16)
    veldnaamsurface = veldnaamfont.render(race.veld, 4, white)
    gameDisplay.blit(veldnaamsurface, (347 + (baan - 1) * 640, 133))

    racenaamfont = pygame.font.SysFont("arial", 16)
    racenaamsurface = racenaamfont.render(race.race, 4, white)
    gameDisplay.blit(racenaamsurface, (347 + (baan - 1) * 640, 155))

    draw_bootje(ploeg, baan, gameDisplay)

    draw_rugnummer(ploeg, baan, gameDisplay)

black = (0,0,0)
white = (255,255,255)
yellow = (255, 191, 54)


def draw_rugnummer(ploeg, baan, gameDisplay):
    """Displayed het eventuele rugnummer van de gegeven ploeg in de behorende baan."""
    if len(ploeg.verenigingen) >= 2 and ploeg.stuur.naam == "Cornelis Zwart":
        elf = pygame.image.load('assets/elf.png')
        elf = pygame.transform.scale(elf, (80, 80))

        gameDisplay.blit(elf, (517 + (baan - 1) * 640, 128))

    elif ploeg.rugnummer is not None:

        gameDisplay.blit(pygame.image.load('assets/rugnummersjabloon.png'), (531 + (baan - 1) * 640, 128))
        rugnummer = ploeg.rugnummer
        rugnummer = str(rugnummer)
        if len(rugnummer) == 1:
            rugnummer = "00" + rugnummer
        elif len(rugnummer) == 2:
            rugnummer = "0" + rugnummer
        rugnummerfont = pygame.font.SysFont("arialblack", 32)
        rugnummersurface = rugnummerfont.render(rugnummer, 4, (0, 0, 0))
        gameDisplay.blit(rugnummersurface, (534 + (baan - 1) * 640, 131))


def draw_stuur(nummer, ploeg, baan, aantalroeiers, gameDisplay, jaar):
    if ploeg.stuur is None or ploeg.stuur.naam == "":
        return
    else:
        gameDisplay.blit(pygame.image.load('assets/Stuurheader.png'),
                         (0 + (baan - 1) * 640, (203 + 64 * (nummer + aantalroeiers))))
        roeiernaamfont = pygame.font.SysFont("arial", 27)
        stuursurface = roeiernaamfont.render("Stuur", 4, yellow)
        stuurnaamsurface = roeiernaamfont.render(ploeg.stuur.naam, 4, white)



        gameDisplay.blit(stuursurface, (53 + (baan - 1) * 640, 211 + 64 * (nummer + aantalroeiers)))
        gameDisplay.blit(stuurnaamsurface, (148 + (baan - 1) * 640, 211 + 64 * (nummer + aantalroeiers)))


        verenigingenfont = pygame.font.SysFont("arial", 16)
        verenigingensurface = verenigingenfont.render(ploeg.stuur.vereniging, 4, yellow)
        gameDisplay.blit(verenigingensurface, (459 + (baan - 1) * 640, 216 + 64 * (nummer + aantalroeiers)))

        if ploeg.stuur.vereniging == "NJO" and "H" in ploeg.veld:
            tenuestring = "NJO-H"
        elif ploeg.roeiers[nummer].vereniging == "NJO" and "D" in ploeg.veld:
            tenuestring = "NJO-D"
        else:
            tenuestring = ploeg.roeiers[nummer].vereniging

        tenue = "tenue/" + jaar + "/" + tenuestring + ".png"
        if os.path.exists(tenue) is False:
            tenue = "tenue/" + tenuestring + ".png"
        if os.path.exists(tenue) is True:
            tenue = pygame.image.load(tenue)
            tenue = pygame.transform.scale(tenue, (15, 37))
            gameDisplay.blit(tenue, (501 + (baan - 1) * 640, 208 + 64* (nummer + aantalroeiers)))


def draw_roeierheader(nummer, ploeg, baan, gameDisplay, jaar):
    if "+" in ploeg.boottype or "*" in ploeg.boottype:
        if nummer == 0 and "4" in ploeg.boottype and ploeg.stuur is not None:
            draw_stuur(nummer, ploeg, baan, 4, gameDisplay, jaar)
        elif nummer == 0 and "2" in ploeg.boottype and ploeg.stuur is not None:
            draw_stuur(nummer, ploeg, baan, 2, gameDisplay, jaar)
        elif nummer == 0 and "8" in ploeg.boottype and ploeg.stuur is not None:
            draw_stuur(nummer, ploeg, baan, 8, gameDisplay, jaar)
    if nummer != 0:
        gameDisplay.blit(pygame.image.load('assets/Roeierheader2.png'),
                         (0 + (baan - 1) * 640, (203 + 64 * (nummer - 1))))
        roeiernaamfont = pygame.font.SysFont("arial", 27)


        roeiernummersurface = roeiernaamfont.render(str(nummer), 4, yellow)

        roeiernaamsurface = roeiernaamfont.render(ploeg.roeiers[nummer - 1].naam, 4, white)


        gameDisplay.blit(roeiernummersurface, (53 + (baan - 1) * 640, 211 + 64 * (nummer - 1)))

        gameDisplay.blit(roeiernaamsurface, (148 + (baan - 1) * 640, 211 + 64 * (nummer - 1)))




        verenigingenfont = pygame.font.SysFont("arial", 16)
        verenigingensurface = verenigingenfont.render(ploeg.roeiers[nummer - 1].vereniging, 4, yellow)
        gameDisplay.blit(verenigingensurface, (459 + (baan - 1) * 640, 216 + 64 * (nummer - 1)))

        if ploeg.roeiers[nummer - 1].vereniging == "NJO" and "H" in ploeg.veld:
            tenuestring = "NJO-H"
        elif ploeg.roeiers[nummer - 1].vereniging == "NJO" and "D" in ploeg.veld:
            tenuestring = "NJO-D"
        else:
            tenuestring = ploeg.roeiers[nummer - 1].vereniging

        tenue = "tenue/" + jaar + "/" + tenuestring + ".png"
        if os.path.exists(tenue) is False:
            tenue = "tenue/" + tenuestring + ".png"
        if os.path.exists(tenue) is True:
            tenue = pygame.image.load(tenue)
            tenue = pygame.transform.scale(tenue, (15, 37))
            gameDisplay.blit(tenue, (501 + (baan - 1) * 640, 208 + 64 * (nummer - 1)))


def draw_baan(ploeg, baan, race, gameDisplay, jaar):
    draw_background(baan, gameDisplay)
    if ploeg is None:
        return
    draw_ploegheader(ploeg, baan, gameDisplay, jaar)
    draw_ploegheaderinfo(ploeg, baan, race, gameDisplay)

    if "1" in ploeg.boottype:
        for i in range(0, 2):
            draw_roeierheader(i, ploeg, baan, gameDisplay, jaar)
    elif "2" in ploeg.boottype:
        for i in range(0, 3):
            draw_roeierheader(i, ploeg, baan, gameDisplay, jaar)
    elif "4" in ploeg.boottype:
        for i in range(0, 5):
            draw_roeierheader(i, ploeg, baan, gameDisplay, jaar)
    elif "8" in ploeg.boottype:
        for i in range(0, 9):
            draw_roeierheader(i, ploeg, baan, gameDisplay, jaar)


def draw_race(race, gameDisplay, jaar):
    draw_baan(race.ploeg1, 1, race, gameDisplay, jaar)

    draw_baan(race.ploeg2, 2, race, gameDisplay, jaar)

    draw_baan(race.ploeg3, 3, race, gameDisplay, jaar)

    draw_baan(race.ploeg4, 4, race, gameDisplay, jaar)

    draw_baan(race.ploeg5, 5, race, gameDisplay, jaar)

    draw_baan(race.ploeg6, 6, race, gameDisplay, jaar)


def draw_timetrial(timetrail, gameDisplay, jaar, aantal_schermen):
    aantal_ploegen = len(timetrail.ploegen)
    print(aantal_ploegen)
    for i in range(aantal_ploegen):
        for j in range(1, aantal_schermen+1):
            
            if i + j-1 < aantal_ploegen:
                draw_baan(timetrail.ploegen[i + j-1], aantal_schermen+1-j, timetrail, gameDisplay, jaar)
            else:
                draw_baan(None, aantal_schermen + 1 - j, timetrail, gameDisplay, jaar)
        pygame.display.update()
        time.sleep(1)
        

def roei_pygame(wedstrijd, racenummer, aantal_schermen):
    pygame.init()
    pygame.font.init()

    display_width = aantal_schermen * 640
    display_height = 1080

    if pygame.display.list_modes()[0][0] == 2560:
        os.environ['SDL_VIDEO_WINDOW_POS'] = '-3120, 0'
    else:
        os.environ['SDL_VIDEO_WINDOW_POS'] = '0, 0'

    gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.NOFRAME)
    pygame.display.set_caption('Roei info')

    clock = pygame.time.Clock()
    crashed = False

    # print(pygame.font.get_fonts())
    # print(pygame.display.list_modes()[0][0])
    # font = "arial"

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        if type(wedstrijd[1][racenummer]).__name__ == "Race":
            draw_race(wedstrijd[1][racenummer], gameDisplay, wedstrijd[0])
            pygame.display.update()
            time.sleep(10)
        if type(wedstrijd[1][racenummer]).__name__ == "TimeTrial":
            print("LOL")
            draw_timetrial(wedstrijd[1][racenummer], gameDisplay, wedstrijd[0], aantal_schermen)
        print(type(wedstrijd[1][racenummer]).__name__)
        pygame.display.update()

        

        racenummer = racenummer + 1
        clock.tick(600)

    pygame.quit()
    quit()
