Tappo = -1
NumPrecedente = 0
Crescente = True
NumElementi = 0

NumCorrente = int(input('Inserisci un numero: '))                     
while NumCorrente != -1:                                   
    if NumCorrente < NumPrecedente:
        Crescente = False        
    NumPrecedente = NumCorrente
    NumCorrente = int(input('Inserisci un numero: '))
    NumElementi+=1

NumElementiMinimo = NumElementi >= 2
if NumElementiMinimo:   
    if Crescente:
        print('SI', end='')
    else:
        print('NO', end='')
                        

    
        

