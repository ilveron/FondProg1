AlmenoDueConsecutivi = False
LettereAlfabeto = False
CaratterePrecedente = ''
Carattere = input()

while Carattere != '*':
    if Carattere == CaratterePrecedente and Carattere.isalpha():
        AlmenoDueConsecutivi = True
        LettereAlfabeto = True
        
    CaratterePrecedente = Carattere
    Carattere = input()

if AlmenoDueConsecutivi and LettereAlfabeto:
    print('SI', end='')
else:
    print('NO', end='')
