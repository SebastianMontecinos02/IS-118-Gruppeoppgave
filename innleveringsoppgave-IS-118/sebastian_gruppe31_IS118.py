
# IS-118 Gruppeoppgave
# Sebastian - Interaktiv historie om Erling

print("ERLINGS PROSJEKTGRUPPE")
print("======================")
print()
print("Erling er prosjektleder for en gruppe som skal utvikle")
print("en digital innbyggerportal. Prototypen skal være klar om tre uker.")
print("Gruppen opplever konflikter, og Erling må ta tre viktige beslutninger.")
print()

# BESLUTNING 1: Konflikten mellom Silje og Elias

print("BESLUTNING 1: Silje og Elias")
print("Silje ønsker innovasjon og fleksibilitet.")
print("Elias prioriterer sikkerhet og kostnader.")
print()
print("1. Erling snakker med dem hver for seg og arrangerer et felles møte.")
print("2. Erling unngår konflikten og håper at de løser den selv.")

valg1 = input("Hva velger Erling? Skriv 1 eller 2: ")

if valg1 == "1":
    print()
    print("Erling lytter til begge og arrangerer et strukturert møte.")
    print("De vurderer forslagene ut fra sikkerhet, kostnader og brukervennlighet.")
    konflikt1 = True
elif valg1 == "2":
    print()
    print("Erling griper ikke inn.")
    print("Konflikten vokser, og Silje og Elias samarbeider dårligere.")
    konflikt1 = False
else:
    print("Ugyldig valg. Start programmet på nytt.")
    raise SystemExit

print()
print("Situasjonen utvikler seg videre.")
print()

# BESLUTNING 2: Konflikten mellom Hamdi og Hallgeir

print("BESLUTNING 2: Hamdi og Hallgeir")
print("Hamdi ønsker kontroll gjennom kommunens eksisterende plattform.")
print("Hallgeir ønsker en åpnere løsning for innbyggerdialog.")
print()
print("1. Erling samler dem for å diskutere behov, kostnader og muligheter.")
print("2. Erling venter og håper at de blir enige på egen hånd.")

valg2 = input("Hva velger Erling? Skriv 1 eller 2: ")

if valg2 == "1":
    print()
    print("Erling lar begge forklare synspunktene sine.")
    print("Gruppen vurderer en moderert løsning og sammenligner kostnader og nytte.")
    konflikt2 = True
elif valg2 == "2":
    print()
    print("Uenigheten fortsetter, og frustrasjonen vokser.")
    print("Viktige spørsmål om drift, ressurser og økonomi forblir ubesvart.")
    konflikt2 = False
else:
    print("Ugyldig valg. Start programmet på nytt.")
    raise SystemExit

print()
print("Erling må nå sørge for at gruppen holder motivasjonen oppe.")
print()

# BESLUTNING 3: Motivasjon og fremdrift

print("BESLUTNING 3: Hvordan bevare motivasjonen?")
print()
print("1. Erling tydeliggjør roller, frister og felles mål, og involverer gruppen.")
print("2. Erling fokuserer bare på fristen og lar gruppen håndtere problemene selv.")

valg3 = input("Hva velger Erling? Skriv 1 eller 2: ")

if valg3 == "1":
    print()
    print("Erling fordeler oppgavene tydelig og legger til rette for åpen dialog.")
    print("Gruppemedlemmene vet hva som forventes av dem.")
    motivasjon = True
elif valg3 == "2":
    print()
    print("Gruppen får mindre oppfølging.")
    print("Motivasjonen synker, og samarbeidet kan bli dårligere.")
    motivasjon = False
else:
    print("Ugyldig valg. Start programmet på nytt.")
    raise SystemExit

# HISTORIENS TRE ENDEPUNKTER

print()
print("HISTORIENS SLUTT")
print("=================")

if konflikt1 and konflikt2 and motivasjon:
    print("ENDEPUNKT 1: Tilliten blir gjenopprettet.")
    print("Erling håndterer konfliktene og styrker samarbeidet.")
    print("Gruppen beveger seg fra storming-fasen mot norming-fasen.")

elif not konflikt1 and not konflikt2 and not motivasjon:
    print("ENDEPUNKT 3: Prosjektet mister samhold og blir forsinket.")
    print("Konfliktene vokser, motivasjonen synker og prototypen forsinkes.")

else:
    print("ENDEPUNKT 2: Konfliktene løses delvis.")
    print("Gruppen holder fremdriften, men noen uenigheter gjenstår.")
    print("Erling må fortsette å arbeide med tillit og samarbeid.")