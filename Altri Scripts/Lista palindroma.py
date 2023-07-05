Lista = []
N = int(input('Inserisci qui un numero (valore tappo 0): '))
Tappo = 0

while N != Tappo:
    Lista.append(N)
    N = int(input('Inserisci qui un numero (valore tappo 0): '))

NumeroElementi = len(Lista)

Palindromo = True
ZeroElementi = NumeroElementi == 0

if NumeroElementi > 1:   
    for k in range (0,NumeroElementi//2):
        if Lista[k] != Lista[(NumeroElementi-1)-k]:
            Palindromo = False
            break
elif ZeroElementi:
    print('La lista non contiene alcun elemento.')

if Palindromo and (not ZeroElementi):
    print('La lista è palindroma!', end='')
else:
    print('La lista non è palindroma!', end='')
    



    
    
