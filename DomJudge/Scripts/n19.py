Carattere = input()
CifraPresente = False
if Carattere == '*':
    print('NESSUNA', end='')
else:
    while Carattere != '*':
        if Carattere.isdigit():
            CifraPresente = True
        Carattere = input()

    if CifraPresente:
        print('ALMENO UNA', end='')
    else:
        print('NESSUNA', end='')
        
