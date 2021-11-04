M = input()
Valida = True
AlfabetoInglese = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
  
for k in range (0,len(M)):
    Carattere = M[k]
    if not Carattere.isdigit() and (Carattere not in AlfabetoInglese) and Carattere != '_':
        Valida = False
        break
    if k == 0 and Carattere.isdigit():
        Valida = False
if Valida:
    print('SI', end='')
else:
    print('NO', end='')            




