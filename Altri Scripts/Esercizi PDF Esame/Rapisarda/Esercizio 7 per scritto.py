def main ():
    N=int(input('Inserisci N'))
    Frase=input('Inserisci la frase')
    if N<len(Frase):
        (Lista1,Lista2)=CreaListe (Frase, N)
        if len(Lista1)==len(Lista2):
            Anagramma= CheckRicorsivo (Lista1,Lista2,0)
            if Anagramma==True:
                print ('SI', end="")
            else:
                print ('NO',end="")
        else:
            print ('No',end="")

def CreaListe (A,B):
    Lista1=[]
    Lista2=[]
    for i in range (len(A)):
        if A[i]!=' ':
            if i<=B-1:
                Lista1.append (A[i])
            else:
                Lista2.append (A[i])

    return (Lista1,Lista2)

def CheckRicorsivo (A,B,i):
    if A[i] in B:
        Indice=B.index(A[i])
        A.pop (i)
        B.pop (Indice)
        if len(A)>0:
            return CheckRicorsivo (A,B,i)
        elif len(A)==0 and len(B)==0:
            return True
    else:
        return False

main ()
