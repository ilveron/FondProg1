def GiudiceBuono(Mat, Righe, Colonne):
    Buono = 0
    MaxVotiMagg = 0
    
    for i in range(Righe):
        VotiMagg = 0
        for j in range(Colonne):
            Voto = Mat[i][j]
            if Voto > 5:
                VotiMagg+=1
        if VotiMagg >= MaxVotiMagg:
            MaxVotiMagg = VotiMagg
            Buono = i
    return Buono

def CantantePeggiore(Mat, Righe, Colonne):
    Peggiore = 0
    MaxSommaVoti = 999999999999

    for j in range(Colonne):
        SommaVoti = 0
        for i in range(Righe):
            SommaVoti += Mat[i][j]
        if SommaVoti <= MaxSommaVoti:
            MaxSommaVoti = SommaVoti
            Peggiore = j           
    return Peggiore

def CostruisciMatrice(Mat, Righe, Colonne):
    for i in range(Righe):
        Riga = []
        for j in range(Colonne):
            Riga.append(int(input()))
        Mat.append(Riga)
                    

def main():
    Righe = int(input())
    Colonne = int(input())
    Mat = []
    CostruisciMatrice(Mat, Righe, Colonne)
    print(GiudiceBuono(Mat, Righe, Colonne), end = ' ')
    print(CantantePeggiore(Mat, Righe, Colonne), end='')

main()
