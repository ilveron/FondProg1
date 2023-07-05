Famiglia = ''
CardFamiglia = 0
CardMaxInsieme = 0

N = int(input('Inserisci un numero: '))
Famiglia += str(N)
while N != -1:   
    CardCorrente = 0
    N = int(input('Inserisci un numero: '))
    if N != 0:
        CardCorrente+=1                
    else:
        CardFamiglia+=1
        if CardCorrente > CardMaxInsieme:
            CardMaxInsieme = CardCorrente
    Famiglia += ' ' + str(N)
    

print('Famiglia:', Famiglia)
print('Cardinalità famiglia:', CardFamiglia)
print('Cardinalità massima insieme:', CardMaxInsieme)
    
    
                
        
        
