from prettytable import PrettyTable
personeel = {"1":{"naam":"Iroh", "geslacht": "man", "afdeling": "CEO", "start_jaar":2008, "loon":6000},
        "2":{"naam":"Zuko", "geslacht": "man", "afdeling": "marketing", "start_jaar":2020, "loon":2000},
        "3":{"naam":"Suki", "geslacht": "vrouw", "afdeling": "HR", "start_jaar":2018, "loon":2300},
        "4":{"naam":"Azula", "geslacht": "vrouw", "afdeling": "Sales", "start_jaar":2020, "loon":3000},
        "5":{"naam":"Tai-Li", "geslacht": "vrouw", "afdeling": "Sales", "start_jaar":2020, "loon":2500},
        "6":{"naam":"Ozai", "geslacht": "man", "afdeling": "operations", "start_jaar":2018, "loon":2300},
        "7":{"naam":"Long Feng", "geslacht": "man", "afdeling": "operations", "start_jaar":2023, "loon":2200},
        "8":{"naam":"Sokka","geslacht":"man","afdeling":"marketing","start_jaar":2019,"loon":2100},
        "9":{"naam":"Toph","geslacht":"vrouw","afdeling":"operations","start_jaar":2018,"loon":2300},
        "10":{"naam":"Katara","geslacht":"vrouw","afdeling":"HR","start_jaar":2018,"loon":2500}}
admin = {"naam":"Aang","wachtwoord":"Avatar"}
def toon_personeel():
        info = PrettyTable(["ID", "Naam", "Geslacht", "Afdeling", "Start Jaar", "Loon"])
        for key, value in personeel.items():
                info.add_row(
                        [key, value["naam"], value["geslacht"], value["afdeling"], value["start_jaar"], value["loon"]])
        print(info)
def toon_menu():
        print("1: Toon Personeel")
        print("2: Voeg een personeelslid toe")
        print("3: Voeg personeelsleden toe")
        print("4: Verwijder een personeelslid")
        print("5: Verhoog loon van personeelslid")
        print("6:  Verhoog alle lonen")
        print("7: Toon admins")
        print("8: Gebruik filter")
def toon_personeel():
        info = PrettyTable(["ID", "Naam", "Geslacht", "Afdeling", "Start Jaar", "Loon"])
        for key, value in personeel.items():
                info.add_row(
                        [key, value["naam"], value["geslacht"], value["afdeling"], value["start_jaar"], value["loon"]])
        print(info)
def voeg_personeelslid_toe():
        naam = input("Geef de naam in: ")
        geslacht = input("Geef het Geslacht in (man/vrouw): ")
        afdeling = input("Geef de afdeling in: ")
        start_jaar = int(input("Geef het startjaar in: "))
        loon = int(input("Geef het loon in: "))

        nieuwe_ID = str(len(personeel) + 1)
        personeel[nieuwe_ID] = {"naam": naam, "geslacht": geslacht, "afdeling": afdeling, "start_jaar": start_jaar,
                              "loon": loon}
def voeg_personeelsleden_toe():
        Hoeveel_toevoegen = int(input("Hoeveel Personeelsleden wil je toevoegen?"))
        for nieuwe_collega in range(Hoeveel_toevoegen):
                naam = input("Geef de naam in: ")
                geslacht = input("Geef het Geslacht in (man/vrouw): ")
                afdeling = input("Geef de afdeling in: ")
                start_jaar = int(input("Geef het startjaar in: "))
                loon = int(input("Geef het loon in: "))

                nieuwe_ID = str(len(personeel) + 1)
                personeel[nieuwe_ID] = {"naam": naam, "geslacht": geslacht, "afdeling": afdeling,
                                        "start_jaar": start_jaar,
                                        "loon": loon}
def verwijder__personeel():
        toon_personeel()
        wie_verwijderen = input("Wie wil je verwijderen? Gebruik ID: ")
        while wie_verwijderen not in personeel:
                print("ID niet gevonden, probeer het opnieuw.")
                wie_verwijderen = input("Wie wil je verwijderen? Gebruik ID: ")
        personeel.pop(wie_verwijderen)
        print("Personeelslid is verwijderd")
def verhoog_loon_van_personeelslid():
        toon_personeel()
        wie_verhogen = input("Wiens loon wil je aanpassen? Gebruik ID: ")
        while wie_verhogen not in personeel:
                print("ID niet gevonden, Probeer het opnieuw")
                wie_verhogen = input("Wiens loon wil je aanpassen? Gebruik ID: ")

        verhoging = int(input("Hoeveel is de verhoging?"))
        personeel[wie_verhogen]["loon"] += verhoging
        print("Loon is aangepast!")
def verhoog_alle_lonen():
        verhoging = int(input("Hoeveel is de verhoging?"))
        for key,value in personeel.items():
                value["loon"] += verhoging
        print("Alle lonen zijn verhoogd")
def toon_admins():
        table = PrettyTable(['Naam', 'Wachtwoord'])
        wachtwoord = ""
        for char in admin['wachtwoord']:
                wachtwoord += chr((ord(char) - 97 + 4) % 26 + 97)
        table.add_row([admin['naam'], wachtwoord])
        print(table)
def gebruik_filter():
        print("1: Toon alle mannen/vrouwen")
        print("2: Toon iedereen van een afdeling")
        print("3: Toon iedereen die meer verdient dan x per maand")
        print("4: Toon iedereen die langer dan x jaar in dienst is")
        filter_keuze=input("Wat wil je filteren? ")
        if filter_keuze == "1":
                subkeuze = input("Op wat wil je filteren Man of Vrouw? ")
                if subkeuze.lower() == "man":
                        filter_m = [persoon for id, persoon in personeel.items() if
                                    persoon["geslacht"].lower() == "man"]
                        table = PrettyTable(["Naam", "Afdeling", "Start Jaar", "Loon"])
                        for persoon in filter_m:
                                table.add_row(
                                        [persoon['naam'], persoon['afdeling'], persoon['start_jaar'], persoon['loon']])
                        print(table)
                elif subkeuze.lower() == "vrouw":
                        filter_v = [persoon for id, persoon in personeel.items() if
                                    persoon["geslacht"].lower() == "vrouw"]
                        table = PrettyTable(["Naam", "Afdeling", "Start Jaar", "Loon"])
                        for persoon in filter_v:
                                table.add_row(
                                        [persoon['naam'], persoon['afdeling'], persoon['start_jaar'], persoon['loon']])
                        print(table)
                else:
                        print("Foutieve invoer")
        elif filter_keuze == "2":
                subkeuze = input("Op welke afdeling je filteren? ")
                filter_a = [persoon for id, persoon in personeel.items() if persoon["afdeling"].lower() == subkeuze.lower()]
                table = PrettyTable(["Naam", "Afdeling", "Start Jaar", "Loon"])
                for persoon in filter_a:
                        table.add_row([persoon['naam'], persoon['afdeling'], persoon['start_jaar'], persoon['loon']])
                print(table)
        elif filter_keuze == "3":
                subkeuze = int(input("Vanaf welk loon wil je filteren? "))
                filter_l = [persoon for id, persoon in personeel.items() if persoon["loon"] < subkeuze]
                table = PrettyTable(["Naam", "Afdeling", "Start Jaar", "Loon"])
                for persoon in filter_l:
                        table.add_row([persoon['naam'], persoon['afdeling'], persoon['start_jaar'], persoon['loon']])
                print(table)
        elif filter_keuze=="4":
                subkeuze = int(input("Vanaf welk jaar wil je filteren? "))
                filter_j = [persoon for id, persoon in personeel.items() if persoon["start_jaar"] > subkeuze]
                table = PrettyTable(["Naam", "Afdeling", "Start Jaar", "Loon"])
                for persoon in filter_j:
                        table.add_row([persoon['naam'], persoon['afdeling'], persoon['start_jaar'], persoon['loon']])
                print(table)
def admin_login():
        admin_naam = input("Geef de naam in:")
        admin_wachtwoord = input("Geef het wachtwoord in:")
        while not (admin["naam"] == admin_naam and admin["wachtwoord"] == admin_wachtwoord):
                print("Gebruikersnaam of wachtwoord niet correct, probeer het opnieuw.")
                admin_naam = input("Geef de naam in:")
                admin_wachtwoord = input("Geef het wachtwoord in:")
        if admin["naam"] == admin_naam and admin["wachtwoord"] == admin_wachtwoord:
                print("Welkom", admin_naam)
                toon_menu()

        keuze = input("geef je keuze in")
        while not keuze == "stop":
                if keuze == "1":
                        toon_personeel()
                        print("geef je keuze in:")
                        toon_menu()
                        keuze = input()

                elif keuze == "2":
                        voeg_personeelslid_toe()
                        print("geef je keuze in:")
                        toon_menu()
                        keuze = input()

                elif keuze == "3":
                        voeg_personeelsleden_toe()
                        print("geef je keuze in:")
                        toon_menu()
                        keuze = input()
                elif keuze == "4":
                        verwijder__personeel()
                        print("geef je keuze in:")
                        toon_menu()
                        keuze = input()
                elif keuze == "5":
                        verhoog_loon_van_personeelslid()
                        print("geef je keuze in:")
                        toon_menu()
                        keuze = input()
                        toon_menu()
                elif keuze == "6":
                        verhoog_alle_lonen()
                        print("geef je keuze in:")
                        toon_menu()
                        keuze = input()
                elif keuze == "7":
                        toon_admins()
                        print("geef je keuze in:")
                        toon_menu()
                        keuze = input()

                elif keuze == "8":
                        gebruik_filter()
                        print("geef je keuze in:")
                        toon_menu()
                        keuze = input()
                else:
                        print("Foutive Keuze!")
                        print("geef je keuze in:", toon_menu())
                        keuze = input()


def toon_gebruiker_menu():
        print("1: Toon Personeel")
        print("2: Gebruik filter")
        print("3: Admin login")

##################################################################
#Hoofdprogramma
##################################################################

toon_gebruiker_menu()
keuze=input("geef je keuze in")
while not keuze =="stop":
        if keuze == "1":
                toon_personeel()
                print("geef je keuze in:")
                toon_gebruiker_menu()
                keuze = input()

        elif keuze == "2":
                gebruik_filter()
                print("geef je keuze in:")
                toon_gebruiker_menu()
                keuze = input()

        elif keuze == "3":
                admin_login()
                toon_gebruiker_menu()
                keuze = input()
        else:
                print("Foutive Keuze!")
                print("geef je keuze in:", toon_gebruiker_menu())
                keuze = input()


