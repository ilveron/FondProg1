def main ():
    N=int(input())
    Lista=[]
    Lista= CreaLista (1,N,Lista)
    Lista= check (0,N,Lista)
    print (Lista)

def check (i,A,lista):
    if i<len(lista)-1:
        PassoRimozione=int(lista[i+1])
        lista= rimozione (0,lista,PassoRimozione)
        return check(i+1,A,lista)
    else:
        return lista

def rimozione (j,lista,passo):
    indice=j+passo-1
    if indice<=len(lista)-1:
        lista.pop (indice)
        return rimozione(indice,lista,passo)
    else:
        return lista


def CreaLista (A,B,lista):
    if A%2!=0:
        lista.append (int(A))
    if A<B:
        return CreaLista(A+1,B,lista)
    else:
        return lista

main ()
