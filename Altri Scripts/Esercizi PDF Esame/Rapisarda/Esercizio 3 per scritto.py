def main ():
    N=int(input('Quante squadre partecipano:'))
    TABELLONE= CreaTabellone (N)
    RISULTATI= InserisciRisultati (TABELLONE,N)
    classifica=CreaClassifica (N,6,TABELLONE)
    CLASSIFICA= CalcoloClassifica (RISULTATI,N,1,classifica)
    STAMPACLASSIFICA (CLASSIFICA,N)

def CreaTabellone (N):
    Matrice= []
    for i in range (N+1):
        Matrice.append ([])
        for j in range (N+1):
            if i==j:
                Matrice[i].append ('-')
            elif i==0:
                Matrice[i].append(input('Inserisci il nome della squadra:'))
            else:
                Matrice[i].append([])
    for l in range (1,N+1):
        Matrice[l][0]=Matrice[0][l]
    return Matrice

def CreaClassifica (N,A,TABELLONE):
    classifica=[]
    for i in range (N+1):
        classifica.append([])
        for j in range (A):
            if i==0 and j==0:
                classifica[i].append('Nome')
            elif i==0 and j==1:
                classifica[i].append('Punti')
            elif i==0 and j==2:
                classifica[i].append('VittTot')
            elif i==0 and j==3:
                classifica[i].append('Pareggi')
            elif i==0 and j==4:
                classifica[i].append('SconfTot')
            elif i==0 and j==5:
                classifica[i].append('VittCasa')
            else:
                classifica[i].append (0)
    for l in range (1,N+1):
        classifica[l][0]=TABELLONE[0][l]
    return classifica



        
def InserisciRisultati (TABELLONE,N):
    for i in range (1,N+1):
        print ('Inserisci i risultati delle partite in casa della squadra', TABELLONE[i][0])
        for j in range (1,N+1):
            if i!=j:
                print('Contro la squadra', TABELLONE[0][j])
                TABELLONE[i][j]=int(input('Inserisci 1 per vittoria, 2 per sconfitta e 0 per pareggio'))
    return TABELLONE 

def CalcoloClassifica (RISULTATI,N,i,classifica):
    Punti=0
    VittTot=0
    Pareggi=0
    SconfTot=0
    VittCasa=0
    if i<N+1:
        for j in range (1,N+1):
            if RISULTATI[i][j]==0:
                Punti+=1
                Pareggi+=1
            elif RISULTATI[i][j]==1:
                Punti+=3
                VittTot+=1
                VittCasa+=1
            elif RISULTATI[i][j]==2:
                SconfTot+=1
        for l in range (1,N+1):
            if RISULTATI[l][i]==0:
                Punti+=1
                Pareggi+=1
            elif RISULTATI[l][i]==1:
                SconfTot+=1
            elif RISULTATI[l][i]==2:
                Punti+=3
                VittTot+=1
        for x in range (6):
            if x==0:
                classifica[i][x]=(RISULTATI[i][0])
            elif x==1:
                classifica[i][x]=(Punti)
            elif x==2:
                classifica[i][x]=(VittTot)
            elif x==3:
                classifica[i][x]=(Pareggi)
            elif x==4:
                classifica[i][x]= (SconfTot)
            elif x==5:
                classifica[i][x]=(VittCasa)

    if i<N+1:
        return CalcoloClassifica (RISULTATI,N,i+1,classifica)
    else:
        return classifica

def STAMPACLASSIFICA (classifica,N):
    for i in range (1,len(classifica)):
        massimo=maxindex(classifica,i,N)
        for j in range (len(classifica)):
            classifica [i][j],classifica[massimo][j]=classifica[massimo][j],classifica[i][j]

    for l in range (len(classifica)):
        for n in range (6):
            print (classifica[l][n],' ',end="")
        print()

def maxindex (classifica,i,N):
    maxindex=i
    for j in range (i,N+1):
        if j!=N:
            if classifica[j][1]>classifica[j+1][1]:
                maxindex=j
            else:
                maxindex=j+1
    return maxindex
                    


                    
main()
