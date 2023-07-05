Stringa = input()
Tappo = '0'
SecondiTotali = 0
StringheInserite = 1
Valore = 0
while Stringa != Tappo:
    if StringheInserite % 2 == 0:
        if Stringa == 'h':
            SecondiTotali += Valore*3600
        elif Stringa == 'm':
            SecondiTotali += Valore*60
        elif Stringa == 's':
            SecondiTotali += Valore
    else:        
        Valore = int(Stringa)
                    
    Stringa = input()
    StringheInserite += 1

print(SecondiTotali, end='')
