Carattere = input()
StringaFinale = ''

if Carattere == '.':
    print('SI', end='')
else:
    while Carattere != '.':
        StringaFinale += Carattere
        Carattere = input()

    SoloLettereInglesi = StringaFinale.isalpha()

    if SoloLettereInglesi:
        print('SI', end='')
    else:
        print('NO', end='')
        
