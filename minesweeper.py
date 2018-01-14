import math
import time
import random
import copy

def kysy_nimi():
    """kysyy ja palauttaa pelaajan nimen max 30 merkkiä"""
    while True:
        nimi = input(" Anna nimesi: ")
        if not nimi:
            print(" Nimesi ei voi olla tyhjä!\n ")
        elif len(nimi) > 30:
            print(" Nimen maksimipituus on 30 merkkiä!\n ")
        elif nimi[0] == " " or nimi[-1] == " ":
            print(" Nimi ei voi alkaa eikä loppua välilyönnillä!\n  ")
        else:
            return nimi
 
def kysy_kentan_koko():
    """kysyy kentän koon x,y(suurempi kuin 10x10  pienempi kuin 100x100) ja palauttaa sen"""
    min = 5
    max = 25
    print(" Minkä kokoisella kentällä haluaisit pelata?\n ")
    while True:
        kentta = input(" Syötä kentän leveys ja korkeus muodossa x,y tai valitse pieni(1), keskikokoinen(2) tai iso(3): ")
        #tarkistus
        try:
            if kentta == "1":
                return 5, 5
            elif kentta == "2":
                return 10, 10
            elif kentta == "3":
                return 20, 20
            elif len(kentta.split(",")) == 2:
                leveys = int(kentta.split(",")[0])
                korkeus = int(kentta.split(",")[1])
                if min <= leveys <= max and min <= korkeus <= max:
                    return int(leveys), int(korkeus)
                else:
                    print(" Kentän korkeuden ja leveyden arvojen tulee olla välillä {}-{}\n ".format(min, max))
            else:
                print("\n Nyt tapahtui virhe!\n Leveyden arvo, sekä korkeuden arvo tulee syöttää kokonaislukuina ja luvut erottaa toisistaan pilkulla. (leveys,korkeus)\n ")
        except ValueError:
            print("\n Nyt tapahtui virhe!\n Leveyden arvo, sekä korkeuden arvo tulee syöttää kokonaislukuina ja luvut erottaa toisistaan pilkulla(leveys,korkeus)\n   ")
 
                   
def kysy_miinat(kentan_leveys, kentan_korkeus):
    """kysyy miinojen lukumäärän(int) ja palauttaa sen. miinojen pienin/suurin sallittu lukumäärä on 1, (len(korkeus)*len(leveys)) / 2 ja vaikeustaso on tietty prosentuaali kentän koosta """
    #palauttaa miinojen määrän kokonaislukuna kysymällä vaikeustason
    while True:
        vaikeustaso = input("Valitse vaikeustaso Easy(1), Medium(2) Hard(3) DeathMarch(4): ")
        try:
            if int(vaikeustaso) == 1:
                miinat = (kentan_leveys * kentan_korkeus) / 8
                return int(miinat), "Easy"
            elif int(vaikeustaso) == 2:
                miinat = (kentan_leveys * kentan_korkeus) / 6
                return int(miinat), "Medium"
            elif int(vaikeustaso) == 3:
                miinat = (kentan_leveys * kentan_korkeus) / 4
                return int(miinat), "Hard"
            elif int(vaikeustaso) == 4:
                miinat = (kentan_leveys * kentan_korkeus) / 3
                return int(miinat), "DeathMarch"
            else:
                print("Valitse vaikeustaso syöttämällä 1, 2, 3 tai 4. Muita syötteitä ei hyväksytä!")
        except ValueError:
            print("Valitse vaikeustaso syöttämällä 1, 2, 3 tai 4. Muita syötteitä ei hyväksytä!")
   
def nayta_tulokset(tiedosto):
    """näyttää pelattujen pelien tulokset. tulevaisuudessa ehkä järjestääkin ne järkevästi"""
    while True:
        tulokset = input("haluatko nähdä kaikki tulokset Kyllä(y) Ei(n): ")
        if tulokset == "n":
            break
        elif tulokset == "y":
            with open(tiedosto) as tulokset:
                for rivi in tulokset.readlines():
                    rivi = rivi.split(",")
                    print("{} pelasi vaikeustasolla {}, {} vuoroa, kun aikaa kului {} sekuntia. Yritys päättyi {}".format(rivi[0], rivi[1], rivi[3], rivi[2], rivi[4]))
            break
        else:
            continue
def tallenna_tulos(tiedosto, nimi, vaikeustaso, vuorot, aika, tulos):
    with open(tiedosto, "a") as tulokset:
        tulokset.write("{},{},{},{},{}.\n".format(nimi, vaikeustaso, aika, vuorot, tulos))
   
def uusipeli():
    while True:
        uusipeli = input("Pelataanko uudestaan? Kyllä(y) Ei(n): ")
        if uusipeli == "y":
            return 1
        elif uusipeli == "n":
            return 0
        else:
            continue
def tulvataytto(planeetta, x, y, tyhjalista, padded_planeetta):
    lista = []
    lista.append((x, y))
    
    while len(lista) > 0:
        x = lista[-1][0]
        y = lista[-1][1]
        lista.pop()
        
        x1 = x + 1
        y1 = y + 1 
        tyhjalista[y][x] = "0"
        padded_planeetta[y1][x1] = "T"
        if padded_planeetta[y1-1][x1-1] == "0":
            lista.append((x-1, y-1))
        elif padded_planeetta[y1-1][x1-1] != "T":
            tyhjalista[y-1][x-1] = padded_planeetta[y1-1][x1-1]
        
        if padded_planeetta[y1-1][x1] == "0":
            lista.append((x, y-1))
        elif padded_planeetta[y1-1][x1] != "T":
            tyhjalista[y-1][x] = padded_planeetta[y1-1][x1]
        
        if padded_planeetta[y1-1][x1+1] == "0":
            lista.append((x+1, y-1))
        elif padded_planeetta[y1-1][x1+1] != "T":
            tyhjalista[y-1][x+1] = padded_planeetta[y1-1][x1+1]
        
        if padded_planeetta[y1][x1-1] == "0":
            lista.append((x-1, y))
        elif padded_planeetta[y1][x1-1] != "T":
            tyhjalista[y][x-1] = padded_planeetta[y1][x1-1]
        
        if padded_planeetta[y1][x1+1] == "0":
            lista.append((x+1, y))
        elif padded_planeetta[y1][x1+1] != "T":
            tyhjalista[y][x+1] = padded_planeetta[y1][x1+1]
        
        if padded_planeetta[y1+1][x1-1] == "0":
            lista.append((x-1, y+1))
        elif padded_planeetta[y1+1][x1-1] != "T":
            tyhjalista[y+1][x-1] = padded_planeetta[y1+1][x1-1]
        
        if padded_planeetta[y1+1][x1] == "0":
            lista.append((x, y+1))
        elif padded_planeetta[y1+1][x1] != "T":
            tyhjalista[y+1][x] = padded_planeetta[y1+1][x1]
        
        if padded_planeetta[y1+1][x1+1] == "0":
            lista.append((x+1, y+1))
        elif padded_planeetta[y1+1][x1+1] != "T":
            tyhjalista[y+1][x+1] = padded_planeetta[y1+1][x1+1]
    tulosta_kentta(tyhjalista)    
    
def sijoita_miina(kentta, jaljella):
    """Asettaa kentälle yhden miinan satunnaiseen, vapaaseen ruutuun ja palauttaa tämän ruudun koordinaatit."""
       
    miina = random.choice(jaljella)
    x = miina[0]
    y = miina[1]
    kentta[y][x] = "X"
    jaljella = jaljella.remove((x, y))
    return (x, y)
 
def ymparoivat_miinat(planeetta, alkio, padded_planeetta):
    x = alkio[0]
    y = alkio[1]
    lista = []
    lista.append((x, y))
   
    if planeetta[y][x] == " ":
        while len(lista) > 0:
            x = lista[-1][0]
            y = lista[-1][1]
            lista.pop()
            planeetta[y][x] = "~"
            x1 = x + 1
            y1 = y + 1
            miinat = 0
            if padded_planeetta[y1-1][x1-1] == "X":
                miinat = miinat + 1
            if padded_planeetta[y1-1][x1] == "X":
                miinat = miinat + 1
            if padded_planeetta[y1-1][x1+1] == "X":
                miinat = miinat + 1
            if padded_planeetta[y1][x1-1] == "X":
                miinat = miinat + 1
            if padded_planeetta[y1][x1+1] == "X":
                miinat = miinat + 1
            if padded_planeetta[y1+1][x1-1] == "X":
                miinat = miinat + 1
            if padded_planeetta[y1+1][x1] == "X":
                miinat = miinat + 1
            if padded_planeetta[y1+1][x1+1] == "X":
                miinat = miinat + 1
           
           
            miinat = str(miinat)
    return miinat
   
def muodosta_kentta(leveys, korkeus, miinat):
    """Muodostaa kentän jossa on miinat, tyhjää paikkaa ympyröivien miinojen määrät ja palauttaa sen, sekä listan johon on tallennettu miinojen paikat tuplena(x, y)"""
    kentta = []
    for rivi in range(korkeus):
        kentta.append([])
        for sarake in range(leveys):
            kentta[-1].append(" ")
    jaljella = []
    for x in range(len(kentta[0])):
        for y in range(len(kentta)):
            jaljella.append((x, y))
   
    miinapaikat = []
    i = 0
    while i < miinat:  
        miinapaikat.append(sijoita_miina(kentta, jaljella))
        i = i + 1
    #tässä vaiheessa miinat on sijoitettu kenttään ja miinapaikat tiedossa
    #sijoitetaan miinalukuarvot tyhjiin paikkoihin
    tyhjat = []
    while len(kentta[0]) != len(tyhjat):
        tyhjat.append("T")
    padded_kentta1 = copy.deepcopy(kentta)
    padded_kentta1.append(tyhjat)
    padded_kentta1.insert(0, tyhjat)
    for rivi in padded_kentta1:  
        rivi.insert(0, "T")
        rivi.append("T")
    
    for alkio in jaljella:
        kentta[int(alkio[1])][int(alkio[0])] = ymparoivat_miinat(kentta, alkio, padded_kentta1)
    
    tyhjat = []
    while len(kentta[1]) != len(tyhjat):
        tyhjat.append("T")
    padded_kentta = copy.deepcopy(kentta)
    padded_kentta.append(tyhjat)
    padded_kentta.insert(0, tyhjat)
    for rivi in padded_kentta:  
        rivi.insert(0, "T")
        rivi.append("T")
    
    return kentta, miinapaikat, padded_kentta
 
   
   
def kysy_koordinaatit(kentta):
    while True:
        koordinaatit = input("Anna avattavan ruudun koordinaatit muodossa x,y: ")
        if len(koordinaatit.split(",")) == 2:
            try:
                y = int(koordinaatit.split(",")[1])
                x = int(koordinaatit.split(",")[0])
                if 1 <= y <= len(kentta) and 1 <= x <= len(kentta[0]):
                    return (y-1,x-1)
                else:
                    print("koordinaattien on oltava kentän sisäpuolella!".format(min, max))
            except ValueError:
                print("koordinaatit voivat olla vain numeroita!")
        else:
            print("koordinaatit on annettava muodossa x,y!")
 
def tyhjakentta(kentta):
    tyhjakentta = []
    for rivi in range(len(kentta)):
        tyhjakentta.append([])
        for sarake in range(len(kentta[0])):
            tyhjakentta[-1].append(" ")
    return tyhjakentta
   
def pelaa_peli(kentta, miinapaikat):
    """palauttaa pelatut vuorot käytetyn ajan ja päättyikö voittoon vai tappioon"""
    aloitusaika = 0
    aika = 0
    vuorot = 0
    aloitusaika = time.time()
    aukaistut = []
    tyhjalista = []
    tyhjalista = tyhjakentta(kentta)
    while True:
        koordinaatit = kysy_koordinaatit(kentta)
        x = koordinaatit[1]
        y = koordinaatit[0]
        aukaistut.append(1)
        if vuorot == 0:
            if kentta[y][x] == "0":
                tulvataytto(kentta, x, y, tyhjalista, padded_kentta)
                vuorot = vuorot + 1
            elif kentta[y][x] == "X":
                print("Valitsemassasi koordinaatissa oli miina, valitse toinen koordinaatti")
            else:
                v = kentta[y][x]
                tyhjalista[y][x] = v
                tulosta_kentta(tyhjalista)
                vuorot = vuorot + 1
            continue
        vuorot = vuorot + 1  
        if kentta[y][x] == "X":
            sekunnit = int(time.time() - aloitusaika)
            tulosta_kentta(kentta)
            print("Pelasit {} vuoroa, joihin meni {} sekuntia, \n Hävisit pelin RIPRAP".format(vuorot, sekunnit))
            tulos = "Häviöön"
            break
        elif kentta[y][x] == "0":
            tulvataytto(kentta, x, y, tyhjalista, padded_kentta)
            continue
        else:
            v = kentta[y][x]
            tyhjalista[y][x] = v
            tulosta_kentta(tyhjalista)

        if len(miinapaikat) == voitto(tyhjalista):
            sekunnit = int(time.time() - aloitusaika)
            print("Pelasit {} vuoroa, joihin meni {} sekuntia, \n Voitit pelin (^.^)/ ".format(vuorot, sekunnit))
            tulos = "Voittoon"
            break
    return vuorot, sekunnit, tulos
def tulosta_kentta(kentta):
    print("     1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25")
    x = " | "
    i = 1
    for i, rivi in enumerate(kentta):
        if i < 9:
            print("", i+1, "|", x.join(rivi), "|")
        else:
            print(i+1, "|", x.join(rivi), "|")

def voitto(tyhjalista):
    x = 0
    for rivi in tyhjalista:
        for alkio in rivi:
           if alkio.count(" ") == 1:
                x = x + 1
    return x
#MAIN
while True:
    nimi = kysy_nimi()
    print("\n Annoit nimen {}.\n ".format(nimi))
    leveys, korkeus = kysy_kentan_koko()
    miinat, vaikeustaso = kysy_miinat(leveys, korkeus)
    kentta, miinapaikat, padded_kentta = muodosta_kentta(leveys, korkeus, miinat)
 
    vuorot, sekunnit, tulos = pelaa_peli(kentta, miinapaikat)
   
    tallenna_tulos("minesweeper_tulokset.txt", nimi, vaikeustaso, vuorot, sekunnit, tulos)
    nayta_tulokset("minesweeper_tulokset.txt")
    if uusipeli() == 0:
        break