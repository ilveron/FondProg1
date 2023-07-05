def main():
    A=input('Inserisci la frase:')
    Alistato=CreaListaFrase (A)
    B= CreaLista ()
    if len(Alistato)==len(B):
        prop=True
        check= CheckRicorsivo (Alistato,B,0,prop)
        print (check)
    else:
        print ('False')
        
def CreaListaFrase (A):
    Lista=[]
    somma=''
    for i in range (len(A)):
        if A[i]!=' ' and i<len(A)-1:
            somma+=A[i]
        if A[i]!=' ' and i==len(A)-1:
            somma+=A[i]
            Lista.append (somma)
        elif A[i]==' ':
            Lista.append (somma)
            somma=''
    return Lista

def CreaLista ():
    Lista=[]
    N=int(input('Inserisci la lista di interi, inserire -1 per interrompere:'))
    while N!=-1:
        Lista.append (N)
        N=int(input())

    return Lista

def CheckRicorsivo (A,B,i,prop):
    if i<len(A):
        if len(A[i])==B[i]:
            prop=True
            return CheckRicorsivo (A,B,i+1,prop)
        else:
            return False
    else:
        return prop

main()
    
