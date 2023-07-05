NumCaratteriPresenti = 0
Ok = False
CaratterePrecedente = '-'

while not Ok:
    if NumCaratteriPresenti > 0:
        CaratterePrecedente = Carattere
    Carattere = input()
    if Carattere == 'k' and CaratterePrecedente == 'o':
        Ok = True
    else:
        NumCaratteriPresenti+=1

print(NumCaratteriPresenti-1, end='')
    
