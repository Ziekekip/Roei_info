from tkinter import *
import time
from tt_scraper import *
from hs_scraper import *
from main import *
from classes import *


def GUI_maak_wedstrijd():
    print("Wedstrijdlink: " + maak_wedstrijd_link.get())
    print("Wedstrijdnaam: " + maak_wedstrijd_naam.get())


    if "time-team.nl" in maak_wedstrijd_link.get():
        tt_pickle_wedstrijd(tt_maakwedstrijd(maak_wedstrijd_link.get(), maak_wedstrijd_jaar.get()), maak_wedstrijd_naam.get())
    elif "hoesnelwasik.nl" in maak_wedstrijd_link.get():
        hs_pickle_wedstrijd(hs_maak_wedstrijd(maak_wedstrijd_link.get(), maak_wedstrijd_jaar.get()), maak_wedstrijd_naam.get())
    else:
        print("Maat, hoe is dat een roeiwedstrijd?")




def GUI_laad_wedstrijd():
    print("Wedstrijdnaam: " + laad_wedstrijd_naam.get())
    print(int(laad_wedstrijd_nummer.get()))
    roei_pygame(tt_unpickle_wedstrijd(laad_wedstrijd_naam.get()), int(laad_wedstrijd_nummer.get()) - 1, int(laad_scherm_aantal.get()))

window = Tk()
window.title("RoeiersInfo Hoofdmenu")
window.geometry("440x600")
window.resizable(False, False)


title = PhotoImage(file="assets/title.png")
title_label = Label(image=title)
title_label.pack()
title_label.image = title

photo1 = PhotoImage(file="assets/HOL.png").subsample(3).zoom(1)
photo1_label = Label(image=photo1)
photo1_label.place(x=340, y=270)
photo1_label.image = photo1

photo2 = PhotoImage(file="assets/PRO.png").subsample(3).zoom(1)
photo2_label = Label(image=photo2)
photo2_label.place(x=5, y=270)
photo2_label.image = photo2



Label(text='Door Lucas Boogaart').place(x=320, y=580)





Label(text="Hier kan je een wedstrijd maken.").pack()
Label().pack()
loting_text = Label( text="Wat is de link van de loting van de wedstrijd?" )
loting_text.pack()




maak_wedstrijd_link = StringVar(value="https://regatta.time-team.nl/rottebokaal/2019/draw/races.php")
maak_link_entry = Entry( textvariable=maak_wedstrijd_link, width=60)
maak_link_entry.pack()


jaar_text = Label( text="Welk jaar is de wedstrijd?\n(Lustrumjaren gaan uit van hoofdseizoen, dus 2020/2021 = 2021" )
jaar_text.pack()

maak_wedstrijd_jaar = StringVar()
maak_jaar_entry = Entry( textvariable=maak_wedstrijd_jaar, width=30)
maak_jaar_entry.pack()


maak_wedstrijdnaam_text = Label( text="Hoe wil je de wedstrijd opslaan?")
maak_wedstrijdnaam_text.pack()

maak_wedstrijd_naam = StringVar(value="rb")
maak_naam_entry = Entry( textvariable=maak_wedstrijd_naam, width=30)
maak_naam_entry.pack()





Label().pack()

maken = Button(text="Maken", fg="black", bg="lightgray", command=GUI_maak_wedstrijd, width=10)
maken.pack()
Label(text="\n\n\n\nHier kan je een wedstrijd inladen\n").pack()



laad_wedstrijdnaam_text = Label( text="Welke wedstrijd wil je laden?")
laad_wedstrijdnaam_text.pack()



laad_wedstrijd_naam = StringVar(value="asopos")
laad_naam_entry = Entry( textvariable=laad_wedstrijd_naam, width=30)
laad_naam_entry.pack()

Label( text="Vanaf de hoeveelste race wil je displayen?").pack()

laad_wedstrijd_nummer = StringVar(value="21")
laad_nummer_entry = Entry( textvariable=laad_wedstrijd_nummer, width=30)
laad_nummer_entry.pack()


Label( text="Hoeveel banen wil je weergeven?").pack()

laad_scherm_aantal = StringVar(value="3")
laad_scherm_entry = Entry( textvariable=laad_scherm_aantal, width=30)
laad_scherm_entry.pack()



Label().pack()

inladen = Button(text="Inladen", fg="black", bg="lightgray", command=GUI_laad_wedstrijd, width=10)
inladen.pack()

window.mainloop()

