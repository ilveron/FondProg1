def main ():
    n=int(input())
    if n>0:
        Lista=crealista (n)
    else:
        print ('Nessuna Lista')
    checkricorsivo (Lista,n,0,0)

def checkricorsivo (lista,A,i,j):
    if i<=A-1:
        if j<A:
            C=lista[i]*lista[j]
            if C in lista and lista.index (C)!=i and lista.index (C)!= j and i!=j:
                print (lista.index (C),i,j)
                return
            else:
                return checkricorsivo (lista,A,i,j+1)
        else:
            return checkricorsivo (lista,A,i+1,0)
    else:
        return print ('Nessun Valore')


def crealista (n):
    lista=[]
    for i in range (n):
        lista.append (int(input()))

    return lista


main ()
