
# Interaktiv historie om Erling


# Hovedmeny for spillet

print("==============================")
print("   PROSJEKTLEDERENS VALG")
print("==============================")
print("\nVelkommen til den interaktive historien!")
print("Erling leder et prosjektteam som utvikler en digital innbyggerportal.")
print("Det har oppstått uenigheter i prosjektgruppen.")
print("Du spiller som Erling, prosjektleder.")
print("Du må ta valg som påvirker teamet og prosjektet.")
print("1. Start spillet")
print("2. Avslutt")

menyvalg = input("Velg 1 eller 2: ")

if menyvalg == "1":
    print("\nDu spiller som Erling!")
elif menyvalg == "2":
    print("\nTakk for at du spilte!")
    quit()
else:
    print("\nUgyldig valg. Start spillet på nytt.")
    quit()

# Start poengsummen
poeng = 0

# Beslutningspunkt 1: Silje og Elias

print("\nBeslutningspunkt 1: Silje og Elias")
print("Silje og Elias er uenige om hvordan en viktig oppgave i prosjektet skal løses.")
print("Begge mener at deres egen løsning er best, og samarbeidet begynner å bli vanskelig.")
print("Resten av teamet merker at konflikten påvirker stemningen.")
print("Erling må velge hvordan han skal løse situasjonen.")

print("Hvordan skal Erling håndtere uenigheten?")
print("1: Ta det opp i plenum (+2 poeng)")
print("2: Individuelle samtaler (+1 poeng)")
print("3: La HR bistå (0 poeng)")

valg1 = input("Velg 1, 2 eller 3: ")

if valg1 == "1":
    print("Gruppen diskuterer konflikten og kan oppnå felles forståelse.")
    poeng += 2
elif valg1 == "2":
    print("Erling snakker med dem hver for seg.")
    poeng += 1
elif valg1 == "3":
    print("HR bistår, men konflikten kan fortsette.")
else:
    print("Ugyldig valg. Prøv spillet på nytt og velg 1, 2 eller 3.")

print("Poeng så langt:", poeng)

# Beslutningspunkt 2: Hamdi og Hallgeir

print("\nBeslutningspunkt 2: Hamdi og Hallgeir")
print("Hamdi vil bruke kommunens eksisterende plattform.")
print("Hallgeir vil ha et mer åpent system der folk kan komme med ideer.")
print("De er uenige om hvilken løsning som er best.")
print("Hvordan skal Erling håndtere uenigheten?")
print("1: Ta initiativ til et felles møte (+1 poeng)")
print("2: Vente og håpe at de løser det selv (0 poeng)")

valg2 = input("Velg 1 eller 2: ")

if valg2 == "1":
    print("Erling arrangerer et felles møte. Gruppen finner en moderat løsning.")
    poeng += 1
elif valg2 == "2":
    print("Erling venter. Konflikten kan vokse og bli vanskeligere å løse.")
else:
    print("Ugyldig valg. Prøv spillet på nytt og velg 1 eller 2.")

print("Poeng så langt:", poeng)


# Beslutningspunkt 3: Motivasjon i teamet

print("\nBeslutningspunkt 3: Motivasjon")
print("Prosjektet nærmer seg en viktig frist, og flere i teamet begynner å bli slitne.")
print("Noen føler at innsatsen deres ikke blir verdsatt, mens andre er bekymret for at prosjektet ikke blir ferdig i tide.")
print("Samarbeidet og motivasjonen begynner å synke.")
print("Erling må velge hvordan han skal løse situasjonen.")
print("Hvordan skal Erling styrke motivasjonen i teamet?")
print("1: Relasjonsbygging og sosiale aktiviteter (+1 poeng)")
print("2: Prioritere framdrift og leveranser (0 poeng)")

valg3 = input("Velg 1 eller 2: ")

if valg3 == "1":
    print("Erling prioriterer teambuilding. Det styrker tilliten og samholdet.")
    poeng += 1
elif valg3 == "2":
    print("Erling prioriterer framdrift og leveranser.")
else:
    print("Ugyldig valg. Prøv spillet på nytt og velg 1 eller 2.")

print("Poeng så langt:", poeng)



# Avslutning: Velg sluttresultat ut fra poengsummen

print("\n--- Slutten på historien ---")
print("Din totale poengsum er:", poeng)

if poeng == 4:
    print("Sluttpunkt 1: Teamet gjenoppretter tillit og går videre til norming-fasen.")
elif poeng >= 1:
    print("Sluttpunkt 2: Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
else:
    print("Sluttpunkt 3: Prosjektet mister samhold og blir forsinket.")

print("\nTakk for at du spilte!")
