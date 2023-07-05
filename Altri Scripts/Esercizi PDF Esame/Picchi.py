def CreaListaInteri(L):
    N = int(input('Inserisci un numero: (termina con -999)\n'))
    Tappo = -999
    while N != Tappo:
        L.append(N)
        N = int(input('Inserisci un numero: (termina con -999)\n'))

def ControllaPicchi(L):
    print(L)
    if len(L) == 1:
        return True
    else:
        Prec = L[0]
        Picco = L[1]
        Succ = L[2]
        if Prec < Picco and Succ < Picco:
            return ControllaPicchi(L[2:])
        else:
            return False
        

def main():
    L = []
    CreaListaInteri(L)
    print(ControllaPicchi(L), end='')
      
main()
