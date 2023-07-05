def InputRisultato(i,j,Squadre):
    RisultatoCorretto = False
    Risultato = ''
    while not RisultatoCorretto:
        Risultato = input('INSERISCI RISULTATO TRA '+str(Squadre[i])+' - '+Squadre[j]+' (1: VITTORIA CASA; 2: VITTORIA OSPITE; 0: PAREGGIO)\n')
        if Risultato == '1' or Risultato == '2' or Risultato == '0':
            RisultatoCorretto = True
    return Risultato

def InputMatrice(Mat, Squadre):
    for i in range(len(Squadre)):
        Riga = []
        for j in range(len(Squadre)):
            if i == j:
                Riga.append('-') #Con il simbolo '-' ignoriamo il risultato
            else:               
                Riga.append(InputRisultato(i,j,Squadre))
        Mat.append(Riga)

def InputSquadre(NumSquadre, VittorieCasa, VittorieTrasferta, Pareggi):
    Lista = []
    for k in range(NumSquadre):
        VittorieCasa.append(0)
        VittorieTrasferta.append(0)
        Pareggi.append(0)
        Lista.append(input('Inserisci il nome della squadra: '))
    return Lista

def AssegnaRisultati(Mat, VittorieCasa, VittorieTrasferta, Pareggi):
    for i in range(len(Mat)):
        for j in range(len(Mat[i])):
            if i == j:
                continue
            Risultato = Mat[i][j]
            if Risultato == '1':
                VittorieCasa[i]+=1
            elif Risultato == '2':
                VittorieTrasferta[j]+=1
            else:
                Pareggi[i]+=1
                Pareggi[j]+=1                                     

def CalcolaPunteggi(VittorieCasa, VittorieOspiti, Pareggi):
    Punteggi = []
    for k in range(len(VittorieCasa)):
        Punteggi.append((VittorieCasa[k]+VittorieOspiti[k])*3+Pareggi[k])     
    return Punteggi
    
    
def main():
    NumSquadre = int(input('Inserisci il numero delle squadre: '))  
    VittorieCasa = []
    Pareggi = []
    VittorieTrasferta = []
    Mat = []
    Squadre = InputSquadre(NumSquadre, VittorieCasa, VittorieTrasferta, Pareggi)
    InputMatrice(Mat, Squadre)
    AssegnaRisultati(Mat, VittorieCasa, VittorieTrasferta, Pareggi)
    Punteggi = CalcolaPunteggi(VittorieCasa, VittorieTrasferta, Pareggi)
    print('La squadra con il maggior numero di vittorie IN CASA è:', Squadre[VittorieCasa.index(max(VittorieCasa))])
    print('La squadra che ha vinto il campionato è:', Squadre[Punteggi.index(max(Punteggi))])
    print('La squadra arrivata ultima è:', Squadre[Punteggi.index(min(Punteggi))])
    for Riga in Mat:
        print(Riga)
        

main()
