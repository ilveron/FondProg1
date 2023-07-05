def main ():
    NOMEA=input ('Inserisci la tua iniziali:(1 lettera)')
    NOMEB=input ('Inserisci l\'iniziale dell\'avversario:(1 lettera)')
    TABELLA= CreaTabella (7,7)
    StartTheFuckinGame (TABELLA,NOMEA,NOMEB,True,0)


def CreaTabella (A,B):
    tabella=[]
    for i in range (A):
        tabella.append ([])
        for j in range (B):
            if i==0:
                tabella[i].append (str(j))
            else:
                tabella[i].append ('0')

    return tabella

def StartTheFuckinGame (tabella,nomeA,nomeB,turno,contatore):
    from random import randint
    while contatore<42:
        StampaTabella (tabella)
        if turno==True:
            print ('E'' il turno del giocatore', nomeA)
            colonna=randint(0,6)
            print('Giocatore ha scelto', colonna)
            print()
            turno=False
            (riga,tabella)=inserisci (tabella, nomeA,colonna)
            contatore+=1
            vittoria= check (tabella, nomeA, riga, colonna)
            if vittoria==True:
                StampaTabella(tabella)
                return (print ('Ha vinto', nomeA))
        else:
            print ('E'' il turno del giocatore', nomeB)
            colonna=randint (0,6)
            print('Giocatore ha scelto', colonna)
            print()
            turno=True
            (riga,tabella)= inserisci (tabella, nomeB,colonna)
            contatore+=1
            vittoria= check (tabella, nomeB, riga, colonna)
            if vittoria==True:
                StampaTabella(tabella)
                return (print ('Ha vinto', nomeB))
    if contatore==42:
        return (print ('Pareggio'))

def check (tabella,nome,riga, colonna):
    #controllo righe
    cont=1
    for j in range (7):
        if j!=6:
            if tabella[riga][j]==nome and tabella[riga][j]==tabella[riga][j+1]:
                cont+=1
                if cont==4:
                    return True
            else:
                cont=1
    if cont==4:
        return True
    #controllo colonne
    cont=1
    for i in range (1,7):
        if i!=6:
            if tabella [i][colonna]==nome and tabella[i][colonna]==tabella[i+1][colonna]:
                cont+=1
                if cont==4:
                    return True
            else:
                cont=1
    if cont==4:
        return True
    #diagonale normale
    indiceI=riga
    indiceJ=colonna
    while indiceI>1 and indiceJ>0:
        indiceI-=1
        indiceJ-=1
    checkDiag= diagonale (tabella, nome, indiceI, indiceJ,1)
    if checkDiag==4:
        return True
    #diagonale inversa
    indiceI=riga
    indiceJ=colonna
    while indiceI>1 and indiceJ<6:
        indiceI-=1
        indiceJ+=1
    checkDiag= diagonaleinversa (tabella, nome, indiceI,indiceJ,1)
    if checkDiag==4:
        return True
    else:
        return False

def diagonaleinversa (tabella,nome,I,J,cont):
    if I<=5 and J>=1:
        if tabella[I][J]==nome and tabella[I][J]==tabella[I+1][J-1]:
            cont+=1
            if cont==4:
                return cont
        else:
            cont=1
    if I==5 or J==1:
        return cont
    else:
        I+=1
        J-=1
        return diagonaleinversa(tabella,nome,I,J,cont)
    
def diagonale (tabella, nome, I, J,cont):
    if I<=5 and J<=5:
        if tabella[I][J]==nome and tabella[I][J]==tabella[I+1][J+1]:
            cont+=1
            if cont==4:
                return cont
        else:
            cont=1
    if I==5 or J==5:
        return cont
    else:
        return diagonale (tabella,nome,I+1,J+1,cont)
    


def inserisci (tabella, nome, j):
    cont=0
    for i in range (6,0,-1):
        if tabella[i][j]=='0':
            tabella[i][j]=nome
            cont=1
            return (i,tabella)
    if cont==0:
        from random import randint
        colonna=randint (0,6)
        print('Giocatore ha scelto', colonna)
        print()
        return inserisci (tabella, nome, colonna)
            
    
def StampaTabella (matrice):
    for i in range (7):
        for j in range (7):
            print (matrice[i][j], ' ',end="")
        print()
    

main()
