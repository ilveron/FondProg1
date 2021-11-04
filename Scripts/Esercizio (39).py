Carattere = input()
AlmenoUnaLettera = False

if Carattere == '.':
    print('SI', end='')
else:
    while Carattere != '.':
        if Carattere.isalpha():
            AlmenoUnaLettera = True
        Carattere = input()

    if not AlmenoUnaLettera:
        print('SI', end='')
    else:
        print('NO', end='')
        
