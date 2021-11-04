Carattere = input()
VocalePresente = bool(0)

while Carattere != '*':
    if Carattere == 'a' or Carattere == 'e' or Carattere == 'i' or Carattere == 'o' or Carattere == 'u':
        VocalePresente = bool(1)
    Carattere = input()

if VocalePresente:
    print('ALMENO 1 VOCALE', end='')
else:
    print('NESSUNA VOCALE', end='')


    
