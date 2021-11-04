def InizializzaMat(Mat, R, C):    
    for i in range(R):
        Riga = []
        for j in range(C):
            Riga.append(0)
        Mat.append(Riga)
        

def GestisciPosLista(Pos, Lunghezza):
    if Pos+1 <= Lunghezza:        
        return Pos+1
    else:
        return 0
    

def main():
    K = int(input())
    Lista = []
    for i in range(K):
        Lista.append(int(input()))
    
    R = int(input())
    C = int(input())
    Mat = []
    InizializzaMat(Mat,R,C)
    PosLista = 0

    InizioR = 0
    InizioC = 0
    FineR = R
    FineC = C
    while InizioR < FineR and InizioC < FineC:        
        for k in range(InizioC, FineC):            
            Mat[InizioR][k] = Lista[PosLista]              
            PosLista = GestisciPosLista(PosLista, len(Lista)-1)
        InizioR+=1
        
        for k in range(InizioR, FineR):
            Mat[k][FineC-1] = Lista[PosLista]      
            PosLista = GestisciPosLista(PosLista, len(Lista)-1)
        FineC-=1

        if InizioR < FineR:
            for k in range(FineC-1, InizioC-1, -1):
                Mat[FineR-1][k] = Lista[PosLista]
                PosLista = GestisciPosLista(PosLista, len(Lista)-1)
            FineR-=1

        if InizioC < FineC:
            for k in range(FineR-1, InizioR-1, -1):
                Mat[k][InizioC] = Lista[PosLista]             
                PosLista = GestisciPosLista(PosLista, len(Lista)-1)
            InizioC+=1

    for Riga in Mat:
        for Elemento in Riga:
            print(Elemento, end='')
        print()
                                            
main()
