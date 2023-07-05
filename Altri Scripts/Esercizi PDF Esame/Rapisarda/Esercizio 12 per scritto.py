def main ():
    TabellaSpese= CreaTabella (32,13)
    RiempiCasualmente (TabellaSpese,32,13)
    StampaTabella(TabellaSpese,32,13)
    checkmensile (TabellaSpese,32,13,1)

def checkmensile (tabella,A,B,mese):
    if mese<B:
        somma=0
        for i in range (1,A):
            somma+=tabella[i][mese]
        media=somma/(A-1)
        for i in range (1,A-2):
            if tabella[i][mese]+tabella[i+1][mese]>media and tabella[i+2][mese]==0:
                print (tabella[0][mese],'la media è',media, 'viene superata dalla spesa dei giorni',tabella[i][0],tabella[i+1][0])
        return checkmensile(tabella,A,B,mese+1)

def RiempiCasualmente (mat, A,B):
    from random import randint
    for i in range (1,A):
        for j in range (1,B):
            mat[i][j]=randint (0,10)

    return mat


def CreaTabella (A,B):
    mesi=['0','GEN','FEB','MAR','APR','MAG','GIU','LUG','AGO','SET','OTT','NOV','DIC']
    cont=1
    mat=[]
    for i in range (A):
        mat.append([])
        for j in range (B):
            if i==0:
                mat[i].append (mesi[j])
            elif j==0:
                mat[i].append(cont)
                cont+=1
            else:
                mat[i].append([])

    return mat

def StampaTabella (Tabella,A,B):
    for i in range (A):
        for j in range (B):
            if i!=0 and 0<=int(Tabella[i][j])<=9:
                print (Tabella[i][j],'   ', end="")
            elif i!=0 and 10<=int(Tabella[i][j])<=99:
                print (Tabella[i][j],'  ', end="")
            else:
                print (Tabella[i][j],' ', end="")
        print()
        



main()
