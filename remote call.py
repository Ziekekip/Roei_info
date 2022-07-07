from main import *
from tt_scraper import *
from classes import *
# ActiefBalans = Ploeg("4+ D2", "Actief Balans",
#                      [Roeier("Lotje Wijnker", "AMP"), Roeier("Sacha Gevers", "AMP"), Roeier("Pieternel Zwart", "AMP"),
#                       Roeier("Myrian Rinzema", "AMP"), Roeier("Hannah Venderbosch", "AMP")], "4+", None, 531, None)
#
# Dames21 = Ploeg("4+ D2", "Dames 21",
#                 [Roeier("Annefleur Dijkhorst", "LAG"), Roeier("Ankemarij Elzinga", "LAG"),
#                  Roeier("Dorris Corsten", "LAG"),
#                  Roeier("Anna Gunnink", "LAG"), Roeier("Anke Elenbaas", "LAG")], "4+", None, 529, None)
#
# ArgoDames1 = Ploeg("4+ D2", "Argo Dames 1",
#                    [Roeier("Sara Almeloo", "ARG"), Roeier("Iris Voskamp", "ARG"), Roeier("Susan Perebolte", "ARG"),
#                     Roeier("Nynke Hoekstra", "ARG"), Roeier("Vera van der Niet", "ARG")], "4+", None, 535, None)
#
# Vidar = Ploeg("4+ D2", "Vidar", [Roeier("Vera van Hinsberg", "VID"), Roeier("Ireen Van der Weerden", "VID"),
#                                  Roeier("Lieke Adamns", "VID"), Roeier("Isa Beuk", "VID"),
#                                  Roeier("Meike Van der Meulen", "VID")], "4+", None, 533, "NER")
#
# Duizendboot = Ploeg("4+ D2", "Duizendboot",
#                     [Roeier("Kim Meewisse", "ORC"), Roeier("Marieke Supar", "ORC"), Roeier("Rosanne Oskam", "ORC"),
#                      Roeier("Mojca Kloos", "ORC"), Roeier("Vera van der Niet", "ORC")], "4+", None, 537, None)
#
# Aegir1 = Ploeg("4+ D2", "Aegir 1", [Roeier("Merel Fentener van Vlissingen", "AEG"), Roeier("Mette Kramer", "AEG"),
#                                     Roeier("Lillian Balhuizen", "AEG"), Roeier("Annet Keijzer", "AEG"),
#                                     Roeier("Nienke Harte", "AEG")], "4+", None, 534, None)
#
# race2 = Race("4+ D2", "A-finale", "16:20", ActiefBalans, Dames21, ArgoDames1, Vidar, Duizendboot, Aegir1)
#
# pro1 = Ploeg("H4+", "Steen Papier Bier",
#              [Roeier("Esmee Talens", "PRO"), Roeier("Jasper Coppen", "LAG"), Roeier("Iwan Hogenboom", "PRO"),
#               Roeier("Nick Borst", "PRO"), Roeier("Ard Suverein", "PRO")], "C4+", None, 58)
# lag1 = Ploeg("DE2+ Cat-A", "Roodkapje",
#              [Roeier("Cornelis Zwart", "TRI"), Roeier("Esmeralda Beuk", "ARG"), Roeier("Pauline Trekman", "AMP")],
#              "2+", None, -1, None)
#
# njo1 = Ploeg("HE8+ Cat-A", "Njord Clubacht",
#              [Roeier("Stuurvrouw", "NJO"), Roeier("Stuurvrouw", "NJO"), Roeier("Stuurvrouw", "NJO"),
#               Roeier("Stuurvrouw", "NJO"), Roeier("Stuurvrouw", "NJO"), Roeier("Stuurvrouw", "NJO"),
#               Roeier("Stuurvrouw", "NJO"), Roeier("Stuurvrouw", "NJO"), Roeier("Stuurvrouw", "NJO"), ], "8+", None, 187,
#              None)
#
# race1 = Race("HE4+ Cat-B", "Voorwedstrijd 1 van 3", "12:00", njo1, pro1, pro1, lag1, None, pro1)





wedstrijdpagina = "https://regatta.time-team.nl/skollcup/2019/draw/races.php"
racelink = "r6cee1159-0733-433a-8c4c-ce7d28fb8421.php"
ploeglink = "entry/926802ad-3b8c-4d46-9b37-52b671390cf9.php"
ploeglink2 = "entry/227a6e29-fc45-4590-b91e-2de131f296b7.php"

# Westelijke = maakwedstrijd("https://regatta.time-team.nl/westelijke/2019/draw/races.php")
# pickle_wedstrijd(Westelijke, "Westelijke")



# rottebokaal = maakwedstrijd("https://regatta.time-team.nl/rottebokaal/2019/draw/races.php")
# pickle_wedstrijd(rottebokaal, "rottebokaal")


# skollcup = maakwedstrijd(wedstrijdpagina)
# pickle_wedstrijd(skollcup, "skollcup")




# skollcup = maakwedstrijd(wedstrijdpagina)
# pickle_wedstrijd(skollcup, "skollcup")



roei_pygame(tt_unpickle_wedstrijd("skollcup"), 0)






#roei_pygame(unpickle_wedstrijd("Westelijke"), 0)

# roei_pygame(unpickle_wedstrijd("rottebokaal"), 4)

#roei_pygame([race2], 0)
# print(naam_naar_afkorting(afkorting_naar_naam("PRO")))
# print(naam_naar_afkorting("Proteus"))