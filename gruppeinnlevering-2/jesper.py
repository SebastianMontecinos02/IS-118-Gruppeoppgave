"""Dette er en historie om Erling, en teamleder som må ta noen avgjørelser.
Hver beslutning han tar vil ha konsekvenser, og det er opp til deg å hjelpe ham.
 Du vil få poeng ut i fra hvilke svar du velger. Lykke til!"""

poeng = 0 

print ("Silje og Elias er uenige, og konflikten har eskalert fra en sakskonflikt til en personkonflikt")
print ("Hva bør Erling gjøre?")
print ("1. Ta det opp i plenum")
print ("2. Individuelle samtaler med Silje og Elias")
print ("3. La HR bistå")

valg1 = input("Ditt valg: ")
while valg1 not in ["1", "2", "3"]:
    print ("Ugyldig valg. Vennligst velg 1, 2 eller 3.")
    valg1 = input("Ditt valg: ")
if valg1 == "1":
    poeng += 2
    print ("Erling tar det opp i plenum. Han henger ikke ut noen, men gir alle en god forståelse av situasjonen.")
elif valg1 == "2":
    poeng += 1
    print ("Erling tar en individuell samtale med Silje og Elias. Han får en bedre forståelse av konflikten, men den er vanskelig å løse.")
else:
    poeng += 0
    print ("Erling lar HR bistå. Det har gått for lang tid, og konflikten er blitt veldig personlig, og HR klarer ikke løse den.")

print (" ")
print ("Hamdi og Hallgeir er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter.")
print ("Det er en sakskonflikt, men frustrasjonen øker hos begge parter.")
print ("Hva bør Erling gjøre?")
print ("1. Ta initiativ til et møte med Hamdi og Hallgeir")
print ("2. Avvente og se om konflikten løser seg selv") 

valg2 = input("Ditt valg: ")
while valg2 not in ["1", "2"]:
    print ("Ugyldig valg. Vennligst velg 1 eller 2.")
    valg2 = input("Ditt valg: ")
if valg2 == "1":
    poeng += 1
    print ("Erling tar initiativ til et møte med Hamdi og Hallgeir. De får bedre forståelse av hverandres syn.")
else:
    poeng += 0
    print ("Erling avventer og ser om konflikten løser seg selv. Konflikten eskalerer, og blir til slutt en personkonflikt.")

print (" ")
print ("Etter en god start begynner motivasjonen og energien i gruppen å bli mindre.")
print ("Hva skal Erling gjøre for å styrke motivasjonen og samarbeidet i gruppa?")
print ("1. Sette av tid til relasjonsbygging og sosiale aktiviteter")
print ("2. Prioritere fremdrift og leveranser")

valg3 = input("Ditt valg: ")
while valg3 not in ["1", "2"]:
    print ("Ugyldig valg. Vennligst velg 1 eller 2.")
    valg3 = input("Ditt valg: ")
if valg3 == "1":
    poeng += 1
    print ("Erling setter av tid til relasjonsbygging og sosiale aktiviteter. Motivasjonen og samarbeidet i gruppa styrkes.")
else:
    poeng += 0
    print ("Erling prioriterer fremdrift og leveranser. Motivasjonen og samarbeidet i gruppas blir enda lavere.")

print (" ")
print ("=== RESULTAT ===")
print ("Du fikk: " + str(poeng) + " av 4 poeng")
print (" ")

if poeng == 4:
    print ("Teamet gjenoppretter tilliten og går tilbake til norming-fasen")
elif poeng >= 1 and poeng <= 3:
    print ("Konflikten løses delvis, men teamet har fortsatt utfordringer med tillit og samarbeid")
else:
    print ("Konflikten eskalerer. Teamet går tilbake til storming-fasen.")    

