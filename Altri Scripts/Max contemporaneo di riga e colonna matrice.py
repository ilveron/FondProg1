def InputMatrice(Mat,R,C):
    for i in range(R):
        Riga = []
        for j in range(C):
            Riga.append(input('Inserire valore della cella ['+str(i)+']['+str(j)+']: '))
        Mat.append(Riga)

def MassimiRigheColonne(Mat,R,C):
    '''
    ColonneTrovate = []
    for i in range(R):
        MassimoRiga = Mat[i][0]
        ColMax = 0
        for j in range(C):
            if Mat[i][j] > MassimoRiga:
                MassimoRiga = Mat[i][j]
                ColMax = j
        if ColMax not in ColonneTrovate:
            MassimoColonna = Mat[i][ColMax]
            RigaMax = i
            for k in range(R):               
                if Mat[k][ColMax] > MassimoColonna:
                    MassimoColonna = Mat[k][ColMax]
                    RigaMax = k
            Massimi.append(Mat[RigaMax][ColMax])
            ColonneTrovate.append(ColMax)
    return Massimi'''
    Massimi = []
    IndiciMaxRiga = []
    IndiciMaxColonna = []
    
    for i in range(R):
        MassimoRiga = Mat[i][0]
        Indici = [i,0]
        for j in range(C):
            print(Mat[i][j], MassimoRiga, Mat[i][j] > MassimoRiga)
            if Mat[i][j] > MassimoRiga:                
                MassimoRiga = Mat[i][j]
                Indici = [i,j]
        IndiciMaxRiga.append(Indici)
    for j in range(C):
        MassimoColonna = Mat[0][j]
        Indici = [0,j]
        for i in range(R):
            print(Mat[i][j], MassimoColonna, Mat[i][j] > MassimoColonna)
            if Mat[i][j] > MassimoColonna:
                MassimoColonna = Mat[i][j]
                Indici = [i,j]                
        IndiciMaxColonna.append(Indici)
    for Elemento in IndiciMaxRiga:
        if Elemento in IndiciMaxColonna:
            Massimi.append(Mat[Elemento[0]][Elemento[1]])
    print('IndiciMaxRiga:', IndiciMaxRiga)
    print('IndiciMaxColonna:', IndiciMaxColonna)
    return Massimi
                
def VisualizzaMatrice(Mat):
    for Riga in Mat:
        print(Riga)
           
def main():
    Mat = []
    Righe = int(input('Numero di righe: '))
    Colonne = int(input('Numero di colonne: '))
    InputMatrice(Mat, Righe, Colonne)
    VisualizzaMatrice(Mat)
    print(MassimiRigheColonne(Mat,Righe,Colonne))


main()    
