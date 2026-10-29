def velg():
    """Spør til spilleren skriver A eller B, og returnerer svaret."""
    svar = input("Ditt valg (A/B): ").upper()
    while svar != "A" and svar != "B":
        svar = input("Ugyldig valg. Skriv A eller B: ").upper()
    return svar


poeng = 0

print("""
- ERLING OG MEDBORGERPORTALEN -
Du er Erling, prosjektleder for kommunens nye medborgerportal.
Teamet er i storming-fasen, og prototypen skal være klar om tre uker.
""")

# Beslutningspunkt 1
print("""1) Silje (UX) og Elias (IT) krangler om teknologi og design.
Konflikten har blitt personlig. Hva gjør du?
  A) Tar enesamtaler først, og samler dem så til et strukturert møte
  B) Tar konflikten opp i plenum""")
if velg() == "A":
    poeng += 1
    print("Du finner årsaken bak uenigheten, og møtet blir saklig.\n")
else:
    print("Alle får samme bilde, men Silje og Elias føler seg uthengt.\n")

# Beslutningspunkt 2
print("""2) Hamdi vil bruke kommunens plattform. Hallgeir vil ha en åpen
portal for innbyggerne. Hva gjør du?
  A) Samler dem til et møte og lager en kost-nytte-vurdering
  B) Venter og håper de løser det selv""")
if velg() == "A":
    poeng += 1
    print("Dere blir enige om en moderert mellomløsning.\n")
else:
    print("Du sparer tid, men frustrasjonen vokser i det stille.\n")

# Beslutningspunkt 3
print("""3) Det er to uker igjen, og teamet er slitent. Hva gjør du?
  A) Holder en teamsamling og lager en oversikt over ansvar og frister
  B) Ber alle jobbe hver for seg mot fristen""")
if velg() == "A":
    poeng += 1
    print("Vi-følelsen kommer tilbake, og alle vet hva de skal gjøre.\n")
else:
    print("Det jobbes mye, men misforståelsene hoper seg opp.\n")

# Endepunkt basert på poengsum
print("Resultat:")
if poeng == 3:
    print("""ENDEPUNKT 1: Tilliten er gjenopprettet.
Prototypen leveres i tide, og teamet går videre til norming-fasen.""")
elif poeng >= 1:
    print("""ENDEPUNKT 2: Konfliktene er bare delvis løst.
En forenklet prototype leveres, men tilliten i teamet er skjør.""")
else:
    print("""ENDEPUNKT 3: Teamet mister samholdet.
Prototypen blir forsinket, og Erling blir kalt inn på teppet.""")

print(f"Du fikk {poeng} av 3 poeng. Takk for at du spilte!")