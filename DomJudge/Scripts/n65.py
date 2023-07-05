def ChiediPesi(Pesi):
    for k in range(8):
        Pesi.append(int(input()))

def CalcolaVotiFinali(Matricole, VotiQuesiti, Pesi, VotiFinali, ValoreSoglia):
    cont = 0

    for i in range(70):
        VotoFinale = 0
        for j in range(8):
            VotoFinale += VotiQuesiti[cont]*Pesi[cont%8]
            cont+=1
        VotiFinali.append(VotoFinale)

def EliminaBocciati(VotiFinali, Matricole, ValoreSoglia):
    for k in range(70):
        if VotiFinali[k] < ValoreSoglia:
            Matricole[k] = 'elimina'

    while 'elimina' in Matricole:
        indice=Matricole.index('elimina')
        del Matricole[indice]
        del VotiFinali[indice]
        

def StampaStudentiPromossi(Matricole, VotiFinali):
    for k in range(len(Matricole)):
        VotoFinale = VotiFinali[k]
        Matricola = Matricole[k]
        print(Matricola, VotoFinale)

def CalcolaMinimo(Matricole, VotiFinali):
    PosMinimo = 0
    VotoMinimo = VotiFinali[0]
    for k in range(1, len(Matricole)):
        if VotiFinali[k] <= VotoMinimo:
            VotoMinimo = VotiFinali[k]
            PosMinimo = k
    return PosMinimo
       
def main():
    Pesi = []
    ChiediPesi(Pesi)
    VotiFinali = []
    Matricole = []
    VotiQuesiti = []
    
    for i in range(70):
        InputMatricola = input()
        if len(InputMatricola)<=10:
            Matricole.append(InputMatricola)
        else:
            Matricole.append(InputMatricola[0:10])
        for j in range(8):
            VotiQuesiti.append(int(input()))
    ValoreSoglia = int(input())
    CalcolaVotiFinali(Matricole, VotiQuesiti, Pesi, VotiFinali, ValoreSoglia)
    EliminaBocciati(VotiFinali, Matricole, ValoreSoglia)
    StampaStudentiPromossi(Matricole, VotiFinali)
    if len(Matricole) != 0:
        IndiceMax = max(VotiFinali)        
        MatricolaMax = Matricole[VotiFinali.index(IndiceMax)]
        MatricolaMin = Matricole[CalcolaMinimo(Matricole, VotiFinali)]
        print(len(Matricole), MatricolaMax, MatricolaMin, end='')
        
    
main()
     
