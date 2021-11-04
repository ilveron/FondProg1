AlmenoDueConsecutivi = False
CaratterePrecedente = ''
Carattere = input()

while Carattere != '*':
    if Carattere == CaratterePrecedente:
        AlmenoDueConsecutivi = True

    CaratterePrecedente = Carattere
    Carattere = input()

if AlmenoDueConsecutivi:
    print('SI', end='')
else:
    print('NO', end='')
