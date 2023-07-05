Num = int(input())
NumPrecedente = 0

Crescente = True
Decrescente = True
NumDiMezzo = False
SoloDecrescente = False
NumElementi = 1

while Num != 0:
    if NumPrecedente != 0:
        if not NumDiMezzo:
            if Num < NumPrecedente:            
                NumDiMezzo = True
                if NumElementi <= 2:
                    SoloDecrescente = True
            elif Num == NumPrecedente:
                Crescente = False
        else:
            if Num >= NumPrecedente:
                Descrescente = False
                Crescente = False
    NumPrecedente = Num
    Num = int(input())
    NumElementi+=1

if Crescente and Decrescente and NumDiMezzo and (not SoloDecrescente):
    print('SI', end='')
else:
    print('NO', end='')
