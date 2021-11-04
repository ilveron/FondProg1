Carattere = input()
CaratterePrecedente = '.'
Valido = False
while Carattere != '*':
    if Carattere.isupper():
        if CaratterePrecedente.isupper():
            Valido = True
    if Carattere.islower():
        if CaratterePrecedente == Carattere:
            Valido = True
    CaratterePrecedente = Carattere
    Carattere = input()

if Valido:
    print('SI', end='')
else:
    print('NO', end='')
        
        
    
