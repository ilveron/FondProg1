def InizializzaMatrice(Mat, Dim):    
    for i in range(Dim):
        Riga = []
        for j in range(Dim):
            Riga.append(0)
        Mat.append(Riga)

def VisualizzaPavimento(Pavimento, Dim):
    for i in range(Dim):
        for j in range(Dim):
            if Pavimento[i][j] == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def GestisciComandi(Comandi, Mat, PennaAbbassata, Pos):
    NumeroComandi = 0
    for Comando in Comandi:
        if NumeroComandi<100:
            if Comando == 1:
                PennaAbbassata = False
            elif Comando == 2:
                PennaAbbassata = True
            elif Comando == 3:
                Muovi('est', Mat, PennaAbbassata, Pos)
            elif Comando == 4:
                Muovi('ovest', Mat, PennaAbbassata, Pos)
            elif Comando == 5:
                Muovi('sud', Mat, PennaAbbassata, Pos)
            elif Comando == 6:
                Muovi('nord', Mat, PennaAbbassata, Pos)
            elif Comando == 7:
                VisualizzaPavimento(Mat, 20)
            elif Comando == 9:
                Terminato = True
            NumeroComandi+=1
        else:
            break

def Muovi(Direzione, Mat, PennaAbbassata, Pos):
    Passi = int(input("passi?"))
    print()
    
    Riga = Pos[0]
    Colonna = Pos[1]

    if Direzione == 'est':
        while Colonna < len(Mat[0])-1 and Passi > 0:
            Passi-=1
            Colonna+=1
            if PennaAbbassata:
                Mat[Riga][Colonna] = 1            
    elif Direzione == 'ovest':       
        while Colonna > 0 and Passi > 0:
            Passi-=1
            Colonna-=1
            if PennaAbbassata:
                Mat[Riga][Colonna] = 1            
    elif Direzione == 'sud':
        
        while Riga < len(Mat[0])-1 and Passi > 0:
            Passi-=1
            Riga+=1
            if PennaAbbassata:
                Mat[Riga][Colonna] = 1           
    elif Direzione == 'nord':
        while Riga > 0 and Passi > 0:
            Passi-=1
            Riga-=1
            if PennaAbbassata:
                Mat[Riga][Colonna] = 1
            
            
    Pos[0] = Riga
    Pos[1] = Colonna
        
        
  
def main():
    Pavimento = []
    Comandi = []
    PennaAbbassata = True
    PosizioneTartaruga = [0,0]
    InizializzaMatrice(Pavimento, 20)
    Terminato = False
    

    Comando = int(input())
    while Comando != 9:
        Comandi.append(Comando)
        Comando = int(input())

    GestisciComandi(Comandi, Pavimento, PennaAbbassata, PosizioneTartaruga)
    
main()
