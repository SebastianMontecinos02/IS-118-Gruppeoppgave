
# Beslutningsspill - Konflikthåndtering
# Spilleren er Erling

poeng = 0
fullforte = []

print("===================================")
print("     KONFLIKTHÅNDTERING I TEAMET")
print("===================================")

print("\nVelkommen til beslutningsspillet!")
print("Du spiller som Erling, leder for et team.")
print("Det har oppstått konflikter mellom flere ansatte.")
print("Du må ta tre viktige beslutninger.")
print("Du kan løse situasjonene i valgfri rekkefølge.")

# Hovedmenyen gjentas til alle tre situasjonene er fullført
while len(fullforte) < 3:

    print("\n===================================")
    print("          VELG SITUASJON")
    print("===================================")
    print("1. Silje og Elias")
    print("2. Hallgeir og Hamdi")
    print("3. Motivasjon")

    valg = input("\nVelg situasjon (1, 2 eller 3): ")

    # Sjekker om situasjonen allerede er fullført
    if valg in fullforte:
        print("\nDu har allerede fullført denne situasjonen.")

    # Beslutningspunkt 1 - Silje og Elias
    elif valg == "1":
        print("\nSilje og Elias er uenige om arbeidet.")
        print("Hvordan vil du håndtere konflikten?")
        print("1. Ta det opp i plenum")
        print("2. Gjennomføre individuelle samtaler")
        print("3. La HR bistå")

        valg_silje = input("\nVelg 1, 2 eller 3: ")

        if valg_silje == "1":
            print("\nDet oppstår en åpen konflikt.")
            print("Teamet oppnår etter hvert felles forståelse.")
            poeng += 2
            fullforte.append("1")

        elif valg_silje == "2":
            print("\nDu gjennomfører individuelle samtaler.")
            print("Dette fører til en forenklet implementasjon.")
            poeng += 1
            fullforte.append("1")

        elif valg_silje == "3":
            print("\nHR blir involvert.")
            print("Det oppstår krangel, og konflikten fortsetter.")
            fullforte.append("1")

        else:
            print("\nUgyldig valg. Prøv igjen.")

    # Beslutningspunkt 2 - Hallgeir og Hamdi
    elif valg == "2":
        print("\nHallgeir og Hamdi er uenige.")
        print("Hvordan vil du håndtere situasjonen?")
        print("1. Ta initiativ til et felles møte")
        print("2. Avvente og håpe")

        valg_hallgeir = input("\nVelg 1 eller 2: ")

        if valg_hallgeir == "1":
            print("\nPartene finner en moderert løsning.")
            poeng += 1
            fullforte.append("2")

        elif valg_hallgeir == "2":
            print("\nKonflikten eskalerer uten en løsning.")
            fullforte.append("2")

        else:
            print("\nUgyldig valg. Prøv igjen.")

    # Beslutningspunkt 3 - Motivasjon
    elif valg == "3":
        print("\nMotivasjonen i teamet er dårlig.")
        print("Hva vil du prioritere?")
        print("1. Relasjonsbygging og sosiale aktiviteter")
        print("2. Fremdrift og leveranser")

        valg_motivasjon = input("\nVelg 1 eller 2: ")

        if valg_motivasjon == "1":
            print("\nTeamet gjennomfører teambuilding.")
            print("Samholdet og motivasjonen blir bedre.")
            poeng += 1
            fullforte.append("3")

        elif valg_motivasjon == "2":
            print("\nArbeidet fortsetter, men stemningen blir dårlig.")
            fullforte.append("3")

        else:
            print("\nUgyldig valg. Prøv igjen.")

    else:
        print("\nUgyldig situasjon. Velg 1, 2 eller 3.")

    print("\nPoengsum så langt:", poeng)
    print("Fullførte situasjoner:", len(fullforte), "av 3")

# Sluttpunkter - når alle situasjonene er gjennomført
print("\n===================================")
print("           SPILLET ER FERDIG")
print("===================================")
print("Din totale poengsum er:", poeng)

if poeng == 4:
    print("\nSLUTTPUNKT 1")
    print("Teamet gjenoppretter tillit.")
    print("Dere går videre til norming-fasen.")

elif poeng >= 1:
    print("\nSLUTTPUNKT 2")
    print("Konflikten løses delvis.")
    print("Relasjonene er fortsatt sårbare.")

else:
    print("\nSLUTTPUNKT 3")
    print("Prosjektet mister samhold og forsinkes.")

print("\nTakk for at du spilte!")

