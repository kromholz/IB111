import random

def simulace(n): 
    pozice = 0
    kolo = 0
    pocet_kol = 0
    while pozice < n: # velikost herniho planu
        hod = random.randint(1,6)
        if pozice + hod <= n: #podminka zajistujici, ze se simulace presne trefi na pozici n
            pozice = pozice + hod
            kolo += 1
        if hod != 6: #podminka pro hozeni sestkou
            print "V", kolo,"kole", "padlo", "(",hod,")"
            print "Jsem na pozici", pozice
        else:
            hod2 = random.randint(1,6)
            print "V", kolo , "kole.", "padlo", "(", hod,hod2, ")"



def analyza(n, pocet_opakovani):
    pocet_kol = 0
    for i in range(pocet_opakovani):
        pozice = 0
        kolo = 0
        pocet_kol = 0
        hod2 = 0
        while pozice < n:
            hod = random.randint(1,6)
            if pozice + hod <= n:
                pozice = pozice + hod
                kolo += 1
            if hod != 6:
                continue
            else:
                hod2 = random.randint(1,6)
        pocet_kol = pocet_kol + kolo
              
    avg_rnd_cnt = (float(kolo) / float(pocet_opakovani))
    print "Prumerny pocet kol", avg_rnd_cnt
    
analyza(20,1000)
        
        

