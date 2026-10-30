
# IS-118 Gruppeoppgave
# Sebastian - Interaktiv historie om Erling

print("ERLINGS PROSJEKTGRUPPE")
print("======================")
print()
print("Erling er prosjektleder for en tverrfaglig gruppe som skal")
print("utvikle en digital innbyggerportal for kommunen.")
print("Prototypen skal være klar om tre uker.")
print()
print("Gruppen opplever konflikter, og Erling må ta tre viktige")
print("beslutninger for å sikre samarbeid og fremdrift.")
print()

# BESLUTNING 1: Konflikten mellom Silje og Elias

print("BESLUTNING 1: Silje og Elias")
print("----------------------------")
print("Silje ønsker innovasjon og fleksibilitet.")
print("Elias er opptatt av sikkerhet, kostnader og kontroll.")
print()
print("1. Erling snakker med dem hver for seg og arrangerer")
print("   deretter et felles møte.")
print("2. Erling unngår konflikten og håper at de løser den selv.")
print()

valg1 = input("Hva velger Erling? Skriv 1 eller 2: ")

if valg1 == "1":
    print()
    print("Erling lytter til begge og arrangerer et strukturert møte.")
    print("De diskuterer fordeler og ulemper ved forslagene.")
    print("Gruppen blir bedre kjent med hverandres synspunkter.")
    konflikt1_handtert = True

elif valg1 == "2":
    print()
    print("Erling griper ikke inn i konflikten.")
    print("Silje føler at ideene hennes ikke blir tatt på alvor.")
    print("Elias blir frustrert fordi sikkerhetsspørsmålene ikke avklares.")
    konflikt1_handtert = False

else:
    print("Ugyldig valg. Start programmet på nytt.")
    raise SystemExit

print()
print("SITUASJONEN UTVIKLER SEG")
print("------------------------")

if konflikt1_handtert:
    print("Samarbeidet har blitt bedre, men gruppen må fortsatt")
    print("bestemme hvordan innbyggerportalen skal utformes.")
else:
    print("Uenigheten påvirker resten av gruppen.")
    print("Erling må nå håndtere en ny konflikt før fristen.")

print()

# BESLUTNING 2: Konflikten mellom Hamdi og Hallgeir

print("BESLUTNING 2: Hvordan skal portalen utformes?")
print("---------------------------------------------")
print("Hamdi ønsker å bruke kommunens eksisterende plattform.")
print("Hallgeir ønsker større muligheter for dialog med innbyggerne.")
print()
print("1. Erling samler gruppen for å vurdere behov, kostnader,")
print("   sikkerhet og muligheten for en moderert dialogløsning.")
print("2. Erling utsetter avgjørelsen og lar uenigheten fortsette.")
print()

valg2 = input("Hva velger Erling? Skriv 1 eller 2: ")

if valg2 == "1":
    print()
    print("Erling lar begge forklare forslagene sine.")
    print("Gruppen vurderer en moderert dialogfunksjon på")
    print("kommunens eksisterende plattform.")
    print("De må også undersøke ressursbehov og personvern.")
    konflikt2_handtert = True

elif valg2 == "2":
    print()
    print("Erling utsetter avgjørelsen.")
    print("Gruppen mangler en tydelig plan for portalen.")
    print("Spørsmål om drift, kostnader og innbyggerdialog")
    print("forblir ubesvart.")
    konflikt2_handtert = False

else:
    print("Ugyldig valg. Start programmet på nytt.")
    raise SystemExit

print()
print("FØR DEN SISTE BESLUTNINGEN")
print("--------------------------")

if konflikt2_handtert:
    print("Gruppen har kommet nærmere en løsning.")
    print("Nå må Erling sørge for at alle vet hva de skal gjøre")
    print("for å ferdigstille prototypen innen fristen.")
else:
    print("Det er fortsatt usikkerhet rundt løsningen.")
    print("Samtidig begynner fristen å nærme seg, og")
    print("flere gruppemedlemmer er bekymret for fremdriften.")

print()

# BESLUTNING 3: Motivasjon og fremdrift

print("BESLUTNING 3: Hvordan bevare motivasjonen?")
print("------------------------------------------")
print("Erling må få gruppen til å samarbeide frem mot fristen.")
print()
print("1. Erling tydeliggjør roller, oppgaver og frister,")
print("   samtidig som han involverer og lytter til gruppen.")
print("2. Erling fokuserer bare på fristen og lar gruppen")
print("   håndtere samarbeidsproblemene selv.")
print()

valg3 = input("Hva velger Erling? Skriv 1 eller 2: ")

if valg3 == "1":
    print()
    print("Erling fordeler oppgavene tydelig og setter felles mål.")
    print("Han oppmuntrer til åpen dialog og anerkjenner")
    print("innsatsen til gruppemedlemmene.")
    motivasjon_ivaretatt = True

elif valg3 == "2":
    print()
    print("Erling følger i liten grad opp gruppen.")
    print("Flere blir usikre på ansvaret sitt.")
    print("Motivasjonen og samarbeidet blir dårligere.")
    motivasjon_ivaretatt = False

else:
    print("Ugyldig valg. Start programmet på nytt.")
    raise SystemExit

# HISTORIENS SLUTT

print()
print("HISTORIENS SLUTT")
print("================")

if konflikt1_handtert and konflikt2_handtert and motivasjon_ivaretatt:
    print("ENDEPUNKT 1: TILLIT OG SAMARBEID")
    print()
    print("Erling har håndtert konfliktene på en konstruktiv måte.")
    print("Gruppen finner en mulig løsning for innbyggerportalen")
    print("og får tydeligere roller og felles mål.")
    print("Prototypen kan ferdigstilles innen fristen.")
    print("Gruppen beveger seg fra storming-fasen mot norming-fasen.")

elif not konflikt1_handtert and not konflikt2_handtert and not motivasjon_ivaretatt:
    print("ENDEPUNKT 3: KONFLIKT OG FORSINKELSE")
    print()
    print("Erling har unngått konfliktene og fulgt opp gruppen for lite.")
    print("Samarbeidet bryter sammen, og motivasjonen synker.")
    print("Viktige beslutninger blir ikke tatt i tide.")
    print("Prototypen blir forsinket og får flere svakheter.")

else:
    print("ENDEPUNKT 2: DELVIS LØSNING")
    print()
    print("Erling har lykkes med noen beslutninger, men ikke alle.")
    print("Gruppen kommer videre, men enkelte konflikter")
    print("og utfordringer gjenstår.")
    print("Prototypen blir levert, men noen funksjoner må utsettes.")
    print("Erling må fortsette arbeidet med tillit og samarbeid.")

print()