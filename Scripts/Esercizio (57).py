Espressione = input()
NumCaratteri = len(Espressione)
ParentesizzataBene = True
ParentesiSuperflue = False
NumParentesiAperte = 0
NumParentesiRiempire = 0
UltimoCarattere = ''

if Espressione != '':
    for k in range (0, NumCaratteri):
        Carattere = Espressione[k]
        if Carattere == '(':
            NumParentesiAperte += 1            
        elif Carattere == ')':
            if UltimoCarattere == '(':
                ParentesiSuperflue = True
            NumParentesiAperte -= 1
            if NumParentesiAperte < 0:
                ParentesizzataBene = False
                
        UltimoCarattere = Carattere
    if NumParentesiAperte != 0:
        ParentesizzataBene = False
                    
if ParentesizzataBene:
    print('ok1')
else:
    print('no1')

if not ParentesiSuperflue:
    print('ok2')
else:
    print('no2')
