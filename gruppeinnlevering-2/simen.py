print("========================================")
print("       TEAMETS KONFLIKTHÅNDTERING")
print("========================================")
print()
print("Du skal ta stilling til tre uavhengige hendelser.")
print("Skriv inn nummeret til alternativet du velger.")
print()

total_poeng = 0


# Hendelse 1: Silje og Elias

print("----------------------------------------")
print("HENDELSE 1: SILJE OG ELIAS")
print("----------------------------------------")
print("Hvordan skal uenigheten mellom Silje og Elias håndteres?")
print()
print("1. Ta det opp i plenum")
print("2. Gjennomføre individuelle samtaler")
print("3. La HR bistå")
print()

# While-loopen gjentar spørsmålet helt til brukeren skriver inn
# et gyldig alternativ. Break avslutter loopen når valget er gyldig.
while True:
    valg_1 = input("Velg alternativ 1, 2 eller 3: ")

    if valg_1 == "1":
        print()
        print("Uenigheten utvikler seg til en åpen konflikt.")
        print("Den åpne konflikten fører til en felles forståelse.")
        print("Du får 2 poeng.")
        total_poeng = total_poeng + 2
        break

    elif valg_1 == "2":
        print()
        print("De individuelle samtalene fører til en forenklet implementasjon.")
        print("Du får 1 poeng.")
        total_poeng = total_poeng + 1
        break

    elif valg_1 == "3":
        print()
        print("HR blir involvert, men situasjonen utvikler seg til en krangel.")
        print("Konflikten fortsetter.")
        print("Du får 0 poeng.")
        total_poeng = total_poeng + 0
        break

    else:
        print("Ugyldig valg. Skriv inn 1, 2 eller 3.")
        print()


# Hendelse 2: Hallgeir og Hamdi

print()
print("----------------------------------------")
print("HENDELSE 2: HALLGEIR OG HAMDI")
print("----------------------------------------")
print("Hvordan skal situasjonen mellom Hallgeir og Hamdi håndteres?")
print()
print("1. Ta initiativ til et felles møte")
print("2. Avvente")
print()

# While-loopen fortsetter å kjøre så lenge brukeren ikke har skrevet
# inn et gyldig valg. Break avslutter loopen ved alternativ 1 eller 2.
while True:
    valg_2 = input("Velg alternativ 1 eller 2: ")

    if valg_2 == "1":
        print()
        print("Det felles møtet fører til en moderert løsning.")
        print("Du får 1 poeng.")
        total_poeng = total_poeng + 1
        break

    elif valg_2 == "2":
        print()
        print("Situasjonen eskalerer til konflikt uten at partene finner en løsning.")
        print("Du får 0 poeng.")
        total_poeng = total_poeng + 0
        break

    else:
        print("Ugyldig valg. Skriv inn 1 eller 2.")
        print()


# Hendelse 3: Motivasjon

print()
print("----------------------------------------")
print("HENDELSE 3: MOTIVASJON")
print("----------------------------------------")
print("Hvordan skal teamet prioritere motivasjon og samarbeid?")
print()
print("1. Sette av tid til relasjonsbygging og sosiale aktiviteter")
print("2. Prioritere fremdrift og leveranser")
print()

# While-loopen stiller spørsmålet på nytt dersom brukeren skriver
# noe annet enn 1 eller 2. Break avslutter loopen ved et gyldig valg.
while True:
    valg_3 = input("Velg alternativ 1 eller 2: ")

    if valg_3 == "1":
        print()
        print("Tiltaket fører til teambuilding.")
        print("Du får 1 poeng.")
        total_poeng = total_poeng + 1
        break

    elif valg_3 == "2":
        print()
        print("Prioriteringen fører til dårlig stemning i teamet.")
        print("Du får 0 poeng.")
        total_poeng = total_poeng + 0
        break

    else:
        print("Ugyldig valg. Skriv inn 1 eller 2.")
        print()


# Beregning av sluttresultat

print()
print("========================================")
print("                 RESULTAT")
print("========================================")
print("Total poengsum:", total_poeng, "av 4 mulige poeng.")
print()

if total_poeng == 4:
    print("Teamet gjenoppretter tillit og går videre til norming-fasen.")

elif total_poeng >= 1 and total_poeng <= 3:
    print("Konflikten løses delvis, men relasjonene er fortsatt sårbare.")

else:
    print("Prosjektet mister samhold og forsinkes.")

print()
print("========================================")
print("             PROGRAMMET ER FERDIG")
print("========================================")
